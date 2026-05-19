from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.services.base_service import CRUDBase
from app.models.ticket_mantenimiento import TicketMantenimiento
from app.models.usuario import Usuario
from app.models.maquina import Maquina

class CRUDTicketMantenimiento(CRUDBase[TicketMantenimiento]):
    
    async def crear(self, db: Session, *, obj_in: dict) -> TicketMantenimiento:

        usuario_id = obj_in.get("usuario_id")
        usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
        if not usuario:
            raise HTTPException(status_code=404, detail="No se puede reservar: El usuario no existe.")

        maquina_id = obj_in.get("maquina_id")
        maquina = db.query(Maquina).filter(Maquina.id == maquina_id).first()
        if not maquina:
            raise HTTPException(status_code=404, detail="No se puede reservar: La máquina no existe.")

        return super().crear(db, obj_in=obj_in)

ticket_service = CRUDTicketMantenimiento(TicketMantenimiento)