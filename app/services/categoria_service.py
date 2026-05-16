from sqlalchemy import select
from app.models.categoria_maquina import CategoriaMaquina
from app.services.base_service import CRUDBase

class CRUDCategoria(CRUDBase[CategoriaMaquina]):
    async def buscar_por_nombre(self, db, nombre):
        result = await db.execute(select(self.model).where(self.model.nombre == nombre))
        return result.scalars().first()

categoria_service = CRUDCategoria(CategoriaMaquina)
