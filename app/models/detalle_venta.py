from sqlalchemy import Column, Integer, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.db.base import Base

class DetalleVenta(Base):
    __tablename__ = "detalles_venta"

    id = Column(Integer, primary_key=True)
    cantidad = Column(Integer)
    precio_unitario = Column(Numeric)

    venta_id = Column(Integer, ForeignKey("ventas_tienda.id"))
    producto_id = Column(Integer, ForeignKey("productos_tienda.id"))

    venta = relationship("VentaTienda")
    producto = relationship("ProductoTienda")