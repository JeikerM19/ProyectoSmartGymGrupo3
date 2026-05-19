from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.cliente import Cliente
from app.services.base_service import CRUDBase

class CRUDCliente(CRUDBase[Cliente]):
    async def buscar_por_nombre(self, db: AsyncSession, nombre: str) -> Cliente | None:

        result = await db.execute(
            select(Cliente).where(Cliente.nombre_completo == nombre)
        )

        return result.scalars().first()

cliente_service = CRUDCliente(Cliente)
