from sqlalchemy import Column, Integer, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.db.base import Base

class DetalleVenta(Base):
    __tablename__ = "detalles_venta"

    id = Column(Integer, primary_key=True)
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Numeric(10, 2), nullable=False)
    venta_id = Column(Integer,ForeignKey("ventas_tienda.id"), nullable=False,index=True)
    producto_id = Column(Integer,ForeignKey("productos_tienda.id"), nullable=False,index=True)

    venta = relationship("VentaTienda", back_populates="detalles")
    producto = relationship("ProductoTienda", back_populates="detalles")