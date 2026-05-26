from sqlalchemy import Column, Integer, ForeignKey, Numeric, DateTime, String, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base

class Pago(Base):
    __tablename__ = "pagos"
    __table_args__ = (CheckConstraint("monto > 0", name="check_monto_positivo"),)

    id = Column(Integer, primary_key=True)
    monto = Column(Numeric(10, 2), nullable=False)
    fecha_pago = Column(DateTime, nullable=False, server_default=func.now())
    metodo_pago = Column(String(30), nullable=False)
    membresia_id = Column(Integer, ForeignKey("membresias_cliente.id"), nullable=False, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False, index=True)
    estado = Column(String(20), default="activo", nullable=False)

    membresia = relationship("MembresiaCliente", back_populates="pagos")
    usuario = relationship("Usuario", back_populates="pagos")
