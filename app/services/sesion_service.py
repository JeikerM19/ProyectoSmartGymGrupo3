from sqlalchemy import select, func, String, Integer, Float, Boolean, Date, DateTime
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.services.base_service import CRUDBase
from app.models.sesion_programada import SesionProgramada
from app.models.entrenador import Entrenador
from app.models.disciplina import Disciplina
from typing import Any
from sqlalchemy.orm import joinedload
from datetime import datetime, date

class CRUDSesion(CRUDBase[SesionProgramada]):
    async def obtener_por_entrenador(self, db: AsyncSession, entrenador_id: int):
        result = await db.execute(
            select(SesionProgramada).where(
                SesionProgramada.entrenador_id == entrenador_id,
                SesionProgramada.estado == "activo",
            )
        )
        return result.scalars().all()

    async def obtener_todos(self, db: AsyncSession, *, skip: int = 0, limit: int = 100) -> list[SesionProgramada]:
        result = await db.execute(
            select(SesionProgramada).options(joinedload(SesionProgramada.entrenador)).offset(skip).limit(limit)
        )
        return result.scalars().all()

    async def obtener_paginado(self, db: AsyncSession, *, skip: int = 0, limit: int = 10, filters: dict | None = None):
        query = select(SesionProgramada).options(joinedload(SesionProgramada.entrenador))

        if filters:
            for field, value in filters.items():
                if not hasattr(SesionProgramada, field):
                    continue

                column = getattr(SesionProgramada, field)

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


    async def obtener(self, db: AsyncSession, id: Any) -> SesionProgramada | None:
        result = await db.execute(
            select(SesionProgramada)
            .where(SesionProgramada.id == id)
            .options(joinedload(SesionProgramada.entrenador))
        )
        return result.scalars().first()

    async def crear(self, db: AsyncSession, *, obj_in: dict) -> SesionProgramada:
        hora_inicio = obj_in.get("hora_inicio")
        hora_fin = obj_in.get("hora_fin")
        cupos = obj_in.get("cupos")
        entrenador_id = obj_in.get("entrenador_id")

        if hora_inicio and hora_fin and hora_inicio == hora_fin:
            raise HTTPException(
                status_code=400,
                detail="La hora de inicio no puede ser idéntica a la hora de finalización."
            )

        if cupos is not None and cupos <= 0:
            raise HTTPException(
                status_code=400,
                detail="La cantidad de cupos debe ser un número estrictamente mayor a cero."
            )

        entrenador = await db.execute(
            select(Entrenador).where(Entrenador.id == entrenador_id)
        )
        entrenador = entrenador.scalars().first()

        if not entrenador:
            raise HTTPException(status_code=404, detail="El entrenador no existe.")

        disciplina_id = obj_in.get("disciplina_id")

        disciplina = await db.execute(
            select(Disciplina).where(Disciplina.id == disciplina_id)
        )
        disciplina = disciplina.scalars().first()

        if not disciplina:
            raise HTTPException(status_code=404, detail="La disciplina no existe.")

        if hora_inicio and hora_fin and entrenador_id:
            stmt_solapamiento = select(SesionProgramada).where(
                SesionProgramada.entrenador_id == entrenador_id,
                SesionProgramada.estado == "activo",
                SesionProgramada.hora_inicio < hora_fin,
                SesionProgramada.hora_fin > hora_inicio
            )
            
            result_solapamiento = await db.execute(stmt_solapamiento)
            sesion_conflictiva = result_solapamiento.scalars().first()

            if sesion_conflictiva:
                raise HTTPException(
                    status_code=400,
                    detail=f"El entrenador ya tiene una sesión activa programada en ese rango de horario."
                )

        return await super().crear(db, obj_in=obj_in)

sesion_service = CRUDSesion(SesionProgramada)