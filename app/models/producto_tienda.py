from sqlalchemy import Column, Integer, String, Numeric
from app.db.base import Base

class ProductoTienda(Base):
    __tablename__ = "productos_tienda"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    precio = Column(Numeric)
    stock = Column(Integer)
    estado = Column(String, default="activo")