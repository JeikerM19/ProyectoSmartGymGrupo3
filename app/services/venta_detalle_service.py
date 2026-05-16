from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.services.base_service import CRUDBase
from app.models.detalle_venta import DetalleVenta
from app.models.venta_tienda import VentaTienda
from app.models.producto_tienda import ProductoTienda

class CRUDDetalleVenta(CRUDBase[DetalleVenta]):
    
    def create(self, db: Session, *, obj_in: dict) -> DetalleVenta:
        # 1. Validar que la Venta existe
        venta_id = obj_in.get("venta_id")
        venta = db.query(VentaTienda).filter(VentaTienda.id == venta_id).first()
        if not venta:
            raise HTTPException(status_code=404, detail="No se puede crear el detalle: La venta no existe.")

        producto_tienda = obj_in.get("producto_tienda_id")
        producto = db.query(ProductoTienda).filter(ProductoTienda.id == producto_tienda).first()
        if not producto:
            raise HTTPException(status_code=404, detail="No se puede crear el detalle: El producto no existe.")
        return super().create(db, obj_in=obj_in)