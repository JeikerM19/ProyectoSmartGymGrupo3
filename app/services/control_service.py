from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.services.base_service import CRUDBase
from app.models.control_acceso import TicketMantenimiento
from app.models.cliente import Cliente
from app.models.maquina import Maquina

class CRUDControlAcceso(CRUDBase[TicketMantenimiento]):

    def create(self, db: Session, *, obj_in: dict) -> TicketMantenimiento:
        # 1. Validar que el Usuario existe
        cliente_id = obj_in.get("usuario_id")
        cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
        if not cliente:
            raise HTTPException(status_code=404, detail="No se puede reservar: El cliente no existe.")
        if cliente.estado != "activo":
            raise HTTPException(status_code=403, detail="Acceso denegado: Cliente inactivo o suspendido.")
        return super().create(db, obj_in=obj_in)