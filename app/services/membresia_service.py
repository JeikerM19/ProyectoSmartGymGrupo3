from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.services.base_service import CRUDBase
from app.models.membresia_cliente import MembresiaCliente
from app.models.plan_suscripcion import PlanSuscripcion
from app.models.cliente import Cliente

class CRUDMembresia(CRUDBase[MembresiaCliente]):
    async def crear(self, db: AsyncSession, *, obj_in: dict) -> MembresiaCliente:

        plan_id = obj_in.get("plan_id")
        result_plan = await db.execute(
            select(PlanSuscripcion).where(PlanSuscripcion.id == plan_id)
        )

        plan = result_plan.scalars().first()
        if not plan:
            raise HTTPException(
                status_code=404, detail="El plan de suscripción no existe."
            )

        cliente_id = obj_in.get("cliente_id")

        result_cliente = await db.execute(
            select(Cliente).where(Cliente.id == cliente_id)
        )
        cliente = result_cliente.scalars().first()

        if not cliente:
            raise HTTPException(status_code=404, detail="El cliente no existe.")
        
        return await super().crear(db, obj_in=obj_in)

membresia_service = CRUDMembresia(MembresiaCliente)
