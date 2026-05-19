from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.services.base_service import CRUDBase
from app.models.sesion_programada import SesionProgramada
from app.models.entrenador import Entrenador
from app.models.disciplina import Disciplina

class CRUDSesion(CRUDBase[SesionProgramada]):
    async def obtener_por_entrenador(self, db: AsyncSession, entrenador_id: int):
        result = await db.execute(
            select(SesionProgramada).where(
                SesionProgramada.entrenador_id == entrenador_id,
                SesionProgramada.estado == "activo",
            )
        )
        return result.scalars().all()

    async def crear(self, db: AsyncSession, *, obj_in: dict) -> SesionProgramada:

        entrenador_id = obj_in.get("entrenador_id")

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

        return await super().crear(db, obj_in=obj_in)

sesion_service = CRUDSesion(SesionProgramada)
