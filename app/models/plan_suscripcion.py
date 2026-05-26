from sqlalchemy import Column, Integer, String, Numeric, CheckConstraint
from sqlalchemy.orm import relationship
from app.db.base import Base

class PlanSuscripcion(Base):
    __tablename__ = "planes_suscripcion"
    __table_args__ = (
        CheckConstraint("precio > 0", name="check_precio_plan"),
        CheckConstraint("duracion_dias > 0", name="check_duracion_plan"),
    )

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True, index=True)
    precio = Column(Numeric(10, 2), nullable=False)
    duracion_dias = Column(Integer, nullable=False)
    estado = Column(String(20), default="activo", nullable=False)

    membresias = relationship("MembresiaCliente", back_populates="plan")
