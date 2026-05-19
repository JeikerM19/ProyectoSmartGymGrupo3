from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.services.base_service import CRUDBase
from app.models.evaluacion_biometrica import EvaluacionBiometrica
from app.models.cliente import Cliente

class CRUDEvaluacion(CRUDBase[EvaluacionBiometrica]):
    async def crear(self, db: AsyncSession, *, obj_in: dict) -> EvaluacionBiometrica:

        cliente_id = obj_in.get("cliente_id")
        result = await db.execute(select(Cliente).where(Cliente.id == cliente_id))
        cliente = result.scalars().first()
        
        if not cliente:
            raise HTTPException(status_code=404, detail="El cliente no existe.")

        return await super().crear(db, obj_in=obj_in)

evaluacion_service = CRUDEvaluacion(EvaluacionBiometrica)
