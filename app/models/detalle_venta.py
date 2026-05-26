from sqlalchemy import Column, Integer, ForeignKey, Numeric, String, CheckConstraint
from sqlalchemy.orm import relationship
from app.db.base import Base

class DetalleVenta(Base):
    __tablename__ = "detalles_venta"
    __table_args__ = (
        CheckConstraint("cantidad > 0", name="check_cantidad_detalle"),
        CheckConstraint("precio_unitario > 0", name="check_precio_detalle"),
    )

    id = Column(Integer, primary_key=True)
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Numeric(10, 2), nullable=False)
    venta_id = Column(Integer, ForeignKey("ventas_tienda.id"), nullable=False, index=True)
    producto_id = Column(Integer, ForeignKey("productos_tienda.id"), nullable=False, index=True)
    estado = Column(String(20), default="activo", nullable=False)

    venta = relationship("VentaTienda", back_populates="detalles")
    producto = relationship("ProductoTienda", back_populates="detalles")
