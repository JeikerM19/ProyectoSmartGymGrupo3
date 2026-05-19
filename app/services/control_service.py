from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.services.base_service import CRUDBase
from app.models.control_acceso import ControlAcceso
from app.models.cliente import Cliente

class CRUDControlAcceso(CRUDBase[ControlAcceso]):
    async def crear(self, db: AsyncSession, *, obj_in: dict) -> ControlAcceso:

        cedula = obj_in.get("cedula")
        result = await db.execute(select(Cliente).where(Cliente.cedula == cedula))
        cliente = result.scalars().first()

        if not cliente:
            raise HTTPException(
                status_code=404,
                detail="No se puede registrar acceso: cliente no existe.",
            )

        if cliente.estado != "activo":
            raise HTTPException(
                status_code=403,
                detail="Acceso denegado: cliente inactivo o suspendido.",
            )

        obj_in["cliente_id"] = cliente.id
        obj_in.pop("cedula", None) #elimina la cedula para evitar problemas con el model

        return await super().crear(db, obj_in=obj_in)

control_acceso_service = CRUDControlAcceso(ControlAcceso)
