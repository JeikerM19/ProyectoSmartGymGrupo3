from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Reserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True)
    fecha_reserva = Column(DateTime, nullable=False)
    estado = Column(String, nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False, index=True)
    sesion_id = Column(Integer, ForeignKey("sesiones_programadas.id"), nullable=False, index=True)

    cliente = relationship("Cliente", back_populates="reservas")
    sesion = relationship("SesionProgramada", back_populates="reservas")