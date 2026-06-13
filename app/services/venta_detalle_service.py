from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any
from sqlalchemy.orm import joinedload
from app.services.base_service import CRUDBase
from app.models.detalle_venta import DetalleVenta
from app.models.producto_tienda import ProductoTienda
from app.core.exceptions import ReglaNegocioException

class CRUDDetalleVenta(CRUDBase[DetalleVenta]):
    async def obtener_todos(self, db: AsyncSession) -> list[DetalleVenta]:
        result = await db.execute(
            select(DetalleVenta).options(joinedload(DetalleVenta.producto))
        )
        return result.scalars().all()

    async def obtener(self, db: AsyncSession, id: Any) -> DetalleVenta | None:
        result = await db.execute(
            select(DetalleVenta)
            .where(DetalleVenta.id == id)
            .options(joinedload(DetalleVenta.producto))
        )
        return result.scalars().first()

    async def crear(self, db: AsyncSession, *, obj_in: dict) -> DetalleVenta:
        producto_id = obj_in.get("producto_id")
        cantidad = obj_in.get("cantidad")

        stmt = select(ProductoTienda).where(ProductoTienda.id == producto_id)
        result = await db.execute(stmt)
        producto = result.scalars().first()

        if not producto:
            raise ReglaNegocioException(
                codigo_interno="ERR_PRODUCTO_NO_ENCONTRADO",
                mensaje=f"El producto con ID {producto_id} no existe."
            )

        if producto.stock < cantidad:
            raise ReglaNegocioException(
                codigo_interno="ERR_STOCK_INSUFICIENTE",
                mensaje=f"Stock insuficiente para '{producto.nombre}'. Disponible: {producto.stock}"
            )

        producto.stock -= cantidad
        
        nuevo_detalle = DetalleVenta(**obj_in)
        db.add(nuevo_detalle)
        
        await db.commit() 
        
        await db.refresh(nuevo_detalle)
        
        return nuevo_detalle

detalle_venta_service = CRUDDetalleVenta(DetalleVenta)