from sqlalchemy import Column, Integer, ForeignKey, Date, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class MembresiaCliente(Base):
    __tablename__ = "membresias_cliente"

    id = Column(Integer, primary_key=True)
    fecha_inicio = Column(Date, nullable=False)
    fecha_vencimiento = Column(Date, nullable=False)
    estado = Column(String, nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False, index=True)
    plan_id = Column(Integer, ForeignKey("planes_suscripcion.id"), nullable=False, index=True)
    cliente = relationship("Cliente", back_populates="membresias")
    plan = relationship("PlanSuscripcion", back_populates="membresias")
    pagos = relationship("Pago", back_populates="membresia")