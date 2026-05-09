from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship
from app.db.base import Base

class ProductoTienda(Base):
    __tablename__ = "productos_tienda"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    precio = Column(Numeric(10, 2), nullable=False)
    stock = Column(Integer, nullable=False)

    detalles = relationship("DetalleVenta", back_populates="producto")