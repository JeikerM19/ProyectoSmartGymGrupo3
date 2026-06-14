from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.base_service import CRUDBase
from app.models.plan_suscripcion import PlanSuscripcion
from app.core.exceptions import ReglaNegocioException 

class CRUDPlanSuscripcion(CRUDBase[PlanSuscripcion]):
    
    async def crear(self, db: AsyncSession, *, obj_in: dict) -> PlanSuscripcion:
        nombre = obj_in.get("nombre")

        if nombre:
            stmt = select(PlanSuscripcion).where(PlanSuscripcion.nombre == nombre)
            result = await db.execute(stmt)
            plan_existente = result.scalars().first()

            if plan_existente:
                raise ReglaNegocioException(
                    codigo_interno="ERR_PLAN_DUPLICADO",
                    mensaje=f"No se puede crear el plan: Ya existe un plan de suscripción registrado con el nombre '{nombre}'."
                )

        return await super().crear(db, obj_in=obj_in)

plan = CRUDPlanSuscripcion(PlanSuscripcion)