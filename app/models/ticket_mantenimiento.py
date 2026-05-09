from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import relationship
from app.db.base import Base

class TicketMantenimiento(Base):
    __tablename__ = "tickets_mantenimiento"

    id = Column(Integer, primary_key=True)
    descripcion = Column(String, nullable=False)
    fecha_apertura = Column(DateTime, nullable=False)
    fecha_cierre = Column(DateTime)
    costo = Column(Numeric(10, 2), nullable=False)
    maquina_id = Column(Integer, ForeignKey("maquinas.id"), nullable=False, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False, index=True)

    maquina = relationship("Maquina", back_populates="tickets")
    usuario = relationship("Usuario", back_populates="tickets_mantenimiento")