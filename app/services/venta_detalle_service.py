from sqlalchemy import select, func, String, Integer, Float, Boolean, Date, DateTime
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any
from sqlalchemy.orm import joinedload
from app.services.base_service import CRUDBase
from app.models.detalle_venta import DetalleVenta
from app.models.producto_tienda import ProductoTienda
from app.core.exceptions import ReglaNegocioException
from datetime import datetime, date

class CRUDDetalleVenta(CRUDBase[DetalleVenta]):
    async def obtener_todos(self, db: AsyncSession, *, skip: int = 0, limit: int = 100) -> list[DetalleVenta]:
        result = await db.execute(
            select(DetalleVenta).options(joinedload(DetalleVenta.producto)).offset(skip).limit(limit)
        )
        return result.scalars().all()

    async def obtener_paginado(self, db: AsyncSession, *, skip: int = 0, limit: int = 10, filters: dict | None = None):
        query = select(DetalleVenta).options(joinedload(DetalleVenta.producto))

        if filters:
            for field, value in filters.items():
                if not hasattr(DetalleVenta, field):
                    continue

                column = getattr(DetalleVenta, field)

                try:
                    column_type = column.property.columns[0].type

                    if isinstance(column_type, String):
                        query = query.where(column.ilike(f"%{value}%"))

                    elif isinstance(column_type, Integer):
                        query = query.where(column == int(value))

                    elif isinstance(column_type, Float):
                        query = query.where(column == float(value))

                    elif isinstance(column_type, Boolean):
                        query = query.where(column == (str(value).lower() == "true"))

                    elif isinstance(column_type, Date):
                        query = query.where(column == date.fromisoformat(value))

                    elif isinstance(column_type, DateTime):
                        query = query.where(column == datetime.fromisoformat(value))

                    else:
                        query = query.where(column == value)

                except (ValueError, TypeError, AttributeError):
                    continue

        total_query = select(func.count()).select_from(query.subquery())

        total = await db.scalar(total_query)

        result = await db.execute(query.offset(skip).limit(limit))

        return {"total": total, "items": result.scalars().all()}

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