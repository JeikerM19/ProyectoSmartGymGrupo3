from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.categoria_maquina import CategoriaMaquina
from app.services.base_service import CRUDBase

class CRUDCategoria(CRUDBase[CategoriaMaquina]):
    async def buscar_por_nombre(
        self, db: AsyncSession, nombre: str
    ) -> CategoriaMaquina | None:

        result = await db.execute(
            select(CategoriaMaquina).where(CategoriaMaquina.nombre == nombre)
        )
        return result.scalars().first()

categoria_service = CRUDCategoria(CategoriaMaquina)
