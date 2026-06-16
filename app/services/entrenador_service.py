from sqlalchemy import select, func, String, Integer, Float, Boolean, Date, DateTime
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.base_service import CRUDBase
from app.models.entrenador import Entrenador
from app.models.usuario import Usuario 
from app.core.exceptions import ReglaNegocioException  
from typing import Any
from datetime import datetime, date

class CRUDEntrenador(CRUDBase[Entrenador]):
    async def buscar_por_especialidad(
        self, db: AsyncSession, especialidad: str
    ) -> Entrenador | None:

        result = await db.execute(
            select(Entrenador).where(Entrenador.especialidad == especialidad)
        )
        return result.scalars().first()
    
    async def obtener_todos(self, db: AsyncSession, *, skip: int = 0, limit: int = 100) -> list[Entrenador]:
        result = await db.execute(
            select(Entrenador).options(joinedload(Entrenador.usuario)).offset(skip).limit(limit)
        )
        return result.scalars().all()

    async def obtener_paginado(self, db: AsyncSession, *, skip: int = 0, limit: int = 10, filters: dict | None = None):
        query = select(Entrenador).options(joinedload(Entrenador.usuario))

        if filters:
            for field, value in filters.items():
                if not hasattr(Entrenador, field):
                    continue

                column = getattr(Entrenador, field)

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

    async def obtener(self, db: AsyncSession, id: Any) -> Entrenador | None:
        result = await db.execute(
            select(Entrenador)
            .where(Entrenador.id == id)
            .options(joinedload(Entrenador.usuario))
        )
        return result.scalars().first()

    async def crear(self, db: AsyncSession, *, obj_in: dict) -> Entrenador:
        usuario_id = obj_in.get("usuario_id")

        if usuario_id:
            stmt_usuario = select(Usuario).where(Usuario.id == usuario_id)
            result_usuario = await db.execute(stmt_usuario)
            usuario_existente = result_usuario.scalars().first()

            if not usuario_existente:
                raise ReglaNegocioException(
                    codigo_interno="ERR_USUARIO_NO_ENCONTRADO",
                    mensaje=f"No se puede registrar el entrenador: El usuario con ID {usuario_id} no existe."
                )
        else:
            raise ReglaNegocioException(
                codigo_interno="ERR_USUARIO_REQUERIDO",
                mensaje="El campo 'usuario_id' es obligatorio para registrar un entrenador."
            )

        return await super().crear(db, obj_in=obj_in)

entrenador_service = CRUDEntrenador(Entrenador)