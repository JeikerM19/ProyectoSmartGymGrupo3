from sqlalchemy import Column, Integer, ForeignKey, Date, Numeric, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class EvaluacionBiometrica(Base):
    __tablename__ = "evaluaciones_biometricas"

    id = Column(Integer, primary_key=True)
    fecha = Column(Date, nullable=False)
    peso = Column(Numeric(5, 2), nullable=False)
    estatura = Column(Numeric(5, 2), nullable=False)
    porcentaje_grasa = Column(Numeric(5, 2), nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False, index=True)
    observaciones = Column(String, nullable=True)
    estado = Column(String, default="activo")
    cliente = relationship("Cliente", back_populates="evaluaciones")
