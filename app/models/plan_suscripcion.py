from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship
from app.db.base import Base

class PlanSuscripcion(Base):
    __tablename__ = "planes_suscripcion"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False, unique=True)
    precio = Column(Numeric(10, 2), nullable=False)
    duracion_dias = Column(Integer, nullable=False)
    estado = Column(String, default="activo")
    membresias = relationship("MembresiaCliente", back_populates="plan")

