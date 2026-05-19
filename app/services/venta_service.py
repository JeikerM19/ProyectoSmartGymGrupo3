from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.services.base_service import CRUDBase
from app.models.venta_tienda import VentaTienda
from app.models.cliente import Cliente
from app.models.detalle_venta import DetalleVenta

class CRUDVenta(CRUDBase[VentaTienda]):
    def crear(self, db: Session, *, obj_in: dict) -> VentaTienda:

        cliente_id = obj_in.get("cliente_id")

        cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
        if not cliente:
            raise HTTPException(status_code=404, detail="Cliente no existe")

        detalles = obj_in.pop("detalles", [])

        venta = VentaTienda(**obj_in)
        db.add(venta)
        db.flush()

        total = 0

        for d in detalles:
            detalle = DetalleVenta(
                venta_id=venta.id,
                producto_id=d["producto_id"],
                cantidad=d["cantidad"],
                precio_unitario=d["precio_unitario"],
            )
            total += d["cantidad"] * d["precio_unitario"]
            db.add(detalle)

        venta.total = total

        db.commit()
        db.refresh(venta)

        return venta

venta_service = CRUDVenta(VentaTienda)
