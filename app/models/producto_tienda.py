from sqlalchemy import Column, Integer, String, Numeric, CheckConstraint
from sqlalchemy.orm import relationship
from app.db.base import Base

class ProductoTienda(Base):
    __tablename__ = "productos_tienda"
    __table_args__ = (CheckConstraint("stock >= 0", name="check_stock_positivo"),)

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    precio = Column(Numeric(10, 2), nullable=False)
    stock = Column(Integer, nullable=False)
    estado = Column(String(20), default="activo", nullable=False)

    detalles = relationship("DetalleVenta", back_populates="producto")
