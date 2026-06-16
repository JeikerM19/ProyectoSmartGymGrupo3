from sqlalchemy import select, func, String, Integer, Float, Boolean, Date, DateTime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from app.models.cliente import Cliente
from app.models.usuario import Usuario  
from app.services.base_service import CRUDBase
from typing import Any
from app.core.exceptions import ReglaNegocioException 
from datetime import datetime, date

class CRUDCliente(CRUDBase[Cliente]):
    
    async def buscar_por_nombre(self, db: AsyncSession, nombre: str) -> Cliente | None:
        result = await db.execute(
            select(Cliente).where(Cliente.nombre_completo == nombre)
        )
        return result.scalars().first()

    async def obtener_todos(self, db: AsyncSession, *, skip: int = 0, limit: int = 100) -> list[Cliente]:
        result = await db.execute(
            select(Cliente).options(joinedload(Cliente.usuario)).offset(skip).limit(limit)
        )
        return result.scalars().all()

    async def obtener_paginado(self, db: AsyncSession, *, skip: int = 0, limit: int = 10, filters: dict | None = None):
        query = select(Cliente).options(joinedload(Cliente.usuario))

        if filters:
            for field, value in filters.items():
                if not hasattr(Cliente, field):
                    continue

                column = getattr(Cliente, field)

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

    async def obtener(self, db: AsyncSession, id: Any) -> Cliente | None:
        result = await db.execute(
            select(Cliente)
            .where(Cliente.id == id)
            .options(joinedload(Cliente.usuario))
        )
        return result.scalars().first()

    async def crear(self, db: AsyncSession, *, obj_in: dict) -> Cliente:
        usuario_id = obj_in.get("usuario_id")
        cedula = obj_in.get("cedula")

        if usuario_id:
            stmt_usuario = select(Usuario).where(Usuario.id == usuario_id)
            result_usuario = await db.execute(stmt_usuario)
            usuario_existente = result_usuario.scalars().first()

            if not usuario_existente:
                raise ReglaNegocioException(
                    codigo_interno="ERR_USUARIO_NO_ENCONTRADO",
                    mensaje=f"No se puede crear el cliente: El usuario con ID {usuario_id} no existe."
                )

        if cedula:
            stmt_cedula = select(Cliente).where(Cliente.cedula == cedula)
            result_cedula = await db.execute(stmt_cedula)
            cedula_existente = result_cedula.scalars().first()

            if cedula_existente:
                raise ReglaNegocioException(
                    codigo_interno="ERR_CEDULA_DUPLICADA",
                    mensaje=f"Ya existe un cliente registrado con la cédula {cedula}."
                )

        return await super().crear(db, obj_in=obj_in)

cliente_service = CRUDCliente(Cliente)