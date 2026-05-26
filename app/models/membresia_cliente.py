from sqlalchemy import Column, Integer, ForeignKey, Date, String, CheckConstraint
from sqlalchemy.orm import relationship
from app.db.base import Base

class MembresiaCliente(Base):
    __tablename__ = "membresias_cliente"
    __table_args__ = (
        CheckConstraint(
            "fecha_vencimiento >= fecha_inicio", name="check_fechas_membresia"
        ),
    )

    id = Column(Integer, primary_key=True)
    fecha_inicio = Column(Date, nullable=False)
    fecha_vencimiento = Column(Date, nullable=False)
    estado = Column(String(20), nullable=False, default="activa")
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False, index=True)
    plan_id = Column(Integer, ForeignKey("planes_suscripcion.id"), nullable=False, index=True)

    cliente = relationship("Cliente", back_populates="membresias")
    plan = relationship("PlanSuscripcion", back_populates="membresias")
    pagos = relationship("Pago", back_populates="membresia")
