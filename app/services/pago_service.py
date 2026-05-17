from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.services.base_service import CRUDBase
from app.models.usuario import Usuario
from app.models.membresia_cliente import MembresiaCliente
from app.models.pago import Pago

class CRUDPago(CRUDBase[Pago]):
    
    def crear(self, db: Session, *, obj_in: dict) -> Pago:

        usuario_id = obj_in.get("usuario_id")
        usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        membresia = db.query(MembresiaCliente).filter(MembresiaCliente.usuario_id == usuario_id).first()
        if not membresia:
            raise HTTPException(status_code=404, detail="Membresía no encontrada")

        pago = super().crear(db, obj_in=obj_in)

        membresia.estado = "activa"
        db.commit()

        return pago

pago = CRUDPago(Pago)