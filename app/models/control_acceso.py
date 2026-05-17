from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class ControlAcceso(Base):
    __tablename__ = "control_accesos"

    id = Column(Integer, primary_key=True)
    fecha_hora = Column(DateTime)
    estado = Column(String, default="activo")
    cliente_id = Column(Integer, ForeignKey("clientes.id"))

    cliente = relationship("Cliente")