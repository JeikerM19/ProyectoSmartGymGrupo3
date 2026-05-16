from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.services.base_service import CRUDBase
from app.models.usuario import Usuario
from app.models.membresia_cliente import MembresiaCliente
from app.models.pago import Pago

class CRUDPago(CRUDBase[Pago]):
    
    def create(self, db: Session, *, obj_in: dict) -> Pago:
        # 1. Validar que el Usuario existe
        usuario_id = obj_in.get("usuario_id")
        usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        # 2. Validar que la Membresía del Cliente existe
        membresia = db.query(MembresiaCliente).filter(MembresiaCliente.usuario_id == usuario_id).first()
        if not membresia:
            raise HTTPException(status_code=404, detail="Membresía no encontrada")

        # 3. Crear el Pago
        pago = super().create(db, obj_in=obj_in)

        # 4. Actualizar la Membresía del Cliente
        membresia.estado = "activa"
        db.commit()

        return pago

pago = CRUDPago(Pago)