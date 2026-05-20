from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.services.base_service import CRUDBase
from app.models.ticket_mantenimiento import TicketMantenimiento
from app.models.usuario import Usuario
from app.models.maquina import Maquina

class CRUDTicketMantenimiento(CRUDBase[TicketMantenimiento]):
    async def crear(self, db: AsyncSession, *, obj_in: dict) -> TicketMantenimiento:

        usuario_id = obj_in.get("usuario_id")
        usuario = await db.execute(select(Usuario).where(Usuario.id == usuario_id))
        usuario = usuario.scalars().first()

        if not usuario:
            raise HTTPException(status_code=404, detail="El usuario no existe.")

        maquina_id = obj_in.get("maquina_id")

        maquina = await db.execute(select(Maquina).where(Maquina.id == maquina_id))
        maquina = maquina.scalars().first()

        if not maquina:
            raise HTTPException(status_code=404, detail="La máquina no existe.")

        maquina.estado = "mantenimiento"
        db.add(maquina)

        return await super().crear(db, obj_in=obj_in)

    async def cerrar_ticket(self, db: AsyncSession, *, ticket_id: int, costo: float) -> TicketMantenimiento:
        from datetime import datetime
        
        ticket = await db.get(TicketMantenimiento, ticket_id)
        if not ticket:
            raise HTTPException(status_code=404, detail="El ticket no existe.")
        
        ticket.costo = costo
        ticket.fecha_cierre = datetime.now()
        
        
        maquina = ticket.maquina
        maquina.estado = "activa"
        db.add(maquina)
        
        await db.commit()
        await db.refresh(ticket)
        return ticket
    

ticket_service = CRUDTicketMantenimiento(TicketMantenimiento)