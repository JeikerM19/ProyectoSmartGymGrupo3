from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base

class ControlAcceso(Base):
    __tablename__ = "control_accesos"

    id = Column(Integer, primary_key=True)
    fecha_hora = Column(DateTime, nullable=False,server_default=func.now())
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False, index=True)
    estado = Column(String, default="activo")
    cliente = relationship("Cliente", back_populates="accesos")

