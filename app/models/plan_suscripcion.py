from sqlalchemy import Column, Integer, String, Numeric
from app.db.base import Base

class PlanSuscripcion(Base):
    __tablename__ = "planes_suscripcion"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    precio = Column(Numeric)
    duracion_dias = Column(Integer)
    estado = Column(String, default="activo")