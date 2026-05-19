from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.base_service import CRUDBase
from app.models.entrenador import Entrenador

class CRUDEntrenador(CRUDBase[Entrenador]):
    async def buscar_por_especialidad(
        self, db: AsyncSession, especialidad: str
    ) -> Entrenador | None:

        result = await db.execute(
            select(Entrenador).where(Entrenador.especialidad == especialidad)
        )
        return result.scalars().first()

entrenador_service = CRUDEntrenador(Entrenador)
