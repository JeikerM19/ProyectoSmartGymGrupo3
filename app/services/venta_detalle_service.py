from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.services.base_service import CRUDBase
from app.models.detalle_venta import DetalleVenta
from app.models.venta_tienda import VentaTienda
from app.models.producto_tienda import ProductoTienda

class CRUDDetalleVenta(CRUDBase[DetalleVenta]):
    async def crear(self, db: AsyncSession, *, obj_in: dict) -> DetalleVenta:

        venta_id = obj_in.get("venta_id")

        result_venta = await db.execute(
            select(VentaTienda).where(VentaTienda.id == venta_id)
        )
        venta = result_venta.scalars().first()

        if not venta:
            raise HTTPException(status_code=404, detail="La venta no existe.")

        producto_id = obj_in.get("producto_id")

        result_prod = await db.execute(
            select(ProductoTienda).where(ProductoTienda.id == producto_id)
        )
        producto = result_prod.scalars().first()

        if not producto:
            raise HTTPException(status_code=404, detail="El producto no existe.")

        return await super().crear(db, obj_in=obj_in)

detalle_venta_service = CRUDDetalleVenta(DetalleVenta)
