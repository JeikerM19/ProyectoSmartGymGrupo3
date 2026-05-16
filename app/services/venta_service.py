from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.services.base_service import CRUDBase
from app.models.venta_tienda import VentaTienda
from app.models.cliente import Cliente

class CRUDVenta(CRUDBase[VentaTienda]):
    
    def create(self, db: Session, *, obj_in: dict) -> VentaTienda:
        # 1. Validar que el Cliente existe
        cliente_id = obj_in.get("cliente_id")
        cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
        if not cliente:
            raise HTTPException(status_code=404, detail="No se puede reservar: El cliente no existe.")

        return super().create(db, obj_in=obj_in)