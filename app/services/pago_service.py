from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.services.base_service import CRUDBase
from app.models.pago import Pago
from app.models.usuario import Usuario
from app.models.membresia_cliente import MembresiaCliente

class CRUDPago(CRUDBase[Pago]):
    async def crear(self, db: AsyncSession, *, obj_in: dict) -> Pago:

        usuario_id = obj_in.get("usuario_id")
        usuario = await db.execute(select(Usuario).where(Usuario.id == usuario_id))
        usuario = usuario.scalars().first()

        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        membresia = await db.execute(
            select(MembresiaCliente).where(MembresiaCliente.cliente_id == usuario.id)
        )
        membresia = membresia.scalars().first()

        if not membresia:
            raise HTTPException(status_code=404, detail="Membresía no encontrada")

        obj_in["membresia_id"] = membresia.id

        pago = await super().crear(db, obj_in=obj_in)

        membresia.estado = "activa"
        await db.commit()

        return pago


    async def actualizar(self, db: AsyncSession, *, db_obj: Pago, obj_in: dict) -> Pago:
        raise HTTPException(
            status_code=405, 
            detail="No se puede modificar un pago después de creado. Los pagos son inmutables."
        )
    
   
    async def eliminacion_fisica(self, db: AsyncSession, *, id: int) -> bool:
        raise HTTPException(
            status_code=405,
            detail="No se puede eliminar un pago. Los pagos son inmutables."
        )


pago_service = CRUDPago(Pago)