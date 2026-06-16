from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException
from typing import Any
from sqlalchemy.orm import joinedload
from app.services.base_service import CRUDBase
from app.models.usuario import Usuario
from app.models.rol import Rol
from app.core.security import hash_password
from sqlalchemy.orm import selectinload
from sqlalchemy import func, String, Integer, Float, Boolean, Date, DateTime
from datetime import datetime, date

class CRUDUsuario(CRUDBase[Usuario]):

    async def obtener_todos(self, db: AsyncSession, *, skip: int = 0, limit: int = 100) -> list[Usuario]:
        result = await db.execute(
            select(Usuario).options(joinedload(Usuario.rol)).offset(skip).limit(limit)
        )
        return result.scalars().all()

    async def obtener(self, db: AsyncSession, id: Any) -> Usuario | None:
        result = await db.execute(
            select(Usuario)
            .where(Usuario.id == id)
            .options(joinedload(Usuario.rol))
        )
        return result.scalars().first()
    
    async def crear(self, db: AsyncSession, *, obj_in: dict) -> Usuario:

        rol_id = obj_in.get("rol_id")
        result = await db.execute(select(Rol).filter(Rol.id == rol_id))
        rol = result.scalars().first()

        if not rol:
            raise HTTPException(
                status_code=404, detail="El rol especificado no existe."
            )
    
        email = obj_in.get("email")
        result_email = await db.execute(select(Usuario).filter(Usuario.email == email))
        usuario_existente = result_email.scalars().first()

        if usuario_existente:
            raise HTTPException(
                status_code=400, 
                detail="Este correo electrónico ya está registrado en el sistema."
            )

        obj_in["password"] = hash_password(obj_in["password"])

        nuevo_usuario = await super().crear(db, obj_in=obj_in)
        
        return await self.obtener(db, id=nuevo_usuario.id)

    async def obtener_paginado(self, db: AsyncSession, *, skip: int = 0, limit: int = 10, filters: dict | None = None):
        query = select(Usuario).options(joinedload(Usuario.rol))

        if filters:
            for field, value in filters.items():
                if not hasattr(Usuario, field):
                    continue

                column = getattr(Usuario, field)

                try:
                    column_type = column.property.columns[0].type

                    if isinstance(column_type, String):
                        query = query.where(column.ilike(f"%{value}%"))

                    elif isinstance(column_type, Integer):
                        query = query.where(column == int(value))

                    elif isinstance(column_type, Float):
                        query = query.where(column == float(value))

                    elif isinstance(column_type, Boolean):
                        query = query.where(column == (str(value).lower() == "true"))

                    elif isinstance(column_type, Date):
                        query = query.where(column == date.fromisoformat(value))

                    elif isinstance(column_type, DateTime):
                        query = query.where(column == datetime.fromisoformat(value))

                    else:
                        query = query.where(column == value)

                except (ValueError, TypeError, AttributeError):
                    continue

        total_query = select(func.count()).select_from(query.subquery())

        total = await db.scalar(total_query)

        result = await db.execute(query.offset(skip).limit(limit))

        return {"total": total, "items": result.scalars().all()}

usuario_service = CRUDUsuario(Usuario)
