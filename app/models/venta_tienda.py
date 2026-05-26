from sqlalchemy import Column, Integer, ForeignKey, DateTime, Numeric, String, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base

class VentaTienda(Base):
    __tablename__ = "ventas_tienda"
    __table_args__ = (CheckConstraint("total >= 0", name="check_total_venta"),)

    id = Column(Integer, primary_key=True)
    fecha_venta = Column(DateTime, nullable=False, server_default=func.now())
    total = Column(Numeric(10, 2), nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False, index=True)
    estado = Column(String(20), default="activo", nullable=False)

    cliente = relationship("Cliente", back_populates="ventas")
    detalles = relationship("DetalleVenta", back_populates="venta")
