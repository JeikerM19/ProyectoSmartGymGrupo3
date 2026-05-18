from sqlalchemy import select
from app.models.categoria_maquina import CategoriaMaquina
from app.services.base_service import CRUDBase

class CRUDCategoria(CRUDBase[CategoriaMaquina]):
    def buscar_por_nombre(self, db, nombre):
        return db.query(self.model).filter(self.model.nombre == nombre).first()

categoria_service = CRUDCategoria(CategoriaMaquina)
