from sqlalchemy import Column, Integer, ForeignKey, Date, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class MembresiaCliente(Base):
    __tablename__ = "membresias_cliente"

    id = Column(Integer, primary_key=True)
    fecha_inicio = Column(Date)
    fecha_vencimiento = Column(Date)
    estado = Column(String)

    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    plan_id = Column(Integer, ForeignKey("planes_suscripcion.id"))

    cliente = relationship("Cliente")
    plan = relationship("PlanSuscripcion")