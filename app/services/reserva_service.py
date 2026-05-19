from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.services.base_service import CRUDBase
from app.models.reserva import Reserva
from app.models.cliente import Cliente
from app.models.sesion_programada import SesionProgramada

class CRUDReserva(CRUDBase[Reserva]):
    async def crear(self, db: AsyncSession, *, obj_in: dict) -> Reserva:

        cliente_id = obj_in.get("cliente_id")
        cliente_result = await db.execute(
            select(Cliente).where(Cliente.id == cliente_id)
        )
        cliente = cliente_result.scalars().first()

        if not cliente:
            raise HTTPException(status_code=404, detail="El cliente no existe.")

        sesion_id = obj_in.get("sesion_id")
        sesion_result = await db.execute(
            select(SesionProgramada).where(SesionProgramada.id == sesion_id)
        )
        sesion = sesion_result.scalars().first()

        if not sesion:
            raise HTTPException(status_code=404, detail="La sesión no existe.")

        return await super().crear(db, obj_in=obj_in)

    async def cancelar_reserva(self, db: AsyncSession, reserva_id: int):

        return await self.eliminacion_logica(db, id=reserva_id)

reserva_service = CRUDReserva(Reserva)
