from app.models.cliente import Cliente
from app.services.base_service import CRUDBase

class CRUDCliente(CRUDBase[Cliente]):
    def buscar_por_nombre(self, db, nombre):
        return db.query(self.model).filter(self.model.nombre == nombre).first()

cliente = CRUDCliente(Cliente)
cliente_service = cliente