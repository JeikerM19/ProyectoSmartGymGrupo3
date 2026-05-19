from sqlalchemy import Column, Integer, ForeignKey, Numeric, DateTime, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base

class Pago(Base):
    __tablename__ = "pagos"

    id = Column(Integer, primary_key=True)
    monto = Column(Numeric(10, 2), nullable=False)
    fecha_pago = Column(DateTime, nullable=False, server_default=func.now())
    metodo_pago = Column(String, nullable=False)
    membresia_id = Column(Integer, ForeignKey("membresias_cliente.id"), nullable=False, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False, index=True)
    estado = Column(String, default="activo")

    membresia = relationship("MembresiaCliente", back_populates="pagos")
    usuario = relationship("Usuario", back_populates="pagos")
