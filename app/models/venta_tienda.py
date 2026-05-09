from sqlalchemy import Column, Integer, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import relationship
from app.db.base import Base

class VentaTienda(Base):
    __tablename__ = "ventas_tienda"

    id = Column(Integer, primary_key=True)
    fecha_venta = Column(DateTime)
    total = Column(Numeric)

    cliente_id = Column(Integer, ForeignKey("clientes.id"))

    cliente = relationship("Cliente")