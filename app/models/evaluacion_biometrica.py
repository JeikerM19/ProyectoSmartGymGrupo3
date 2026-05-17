from sqlalchemy import Column, Integer, ForeignKey, Date, Numeric, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class EvaluacionBiometrica(Base):
    __tablename__ = "evaluaciones_biometricas"

    id = Column(Integer, primary_key=True)
    fecha = Column(Date)
    peso = Column(Numeric)
    estatura = Column(Numeric)
    porcentaje_grasa = Column(Numeric)
    estado = Column(String, default="activo")
    cliente_id = Column(Integer, ForeignKey("clientes.id"))

    cliente = relationship("Cliente")