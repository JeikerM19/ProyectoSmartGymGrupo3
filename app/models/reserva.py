from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Reserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True)
    fecha_reserva = Column(DateTime)
    estado = Column(String)

    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    sesion_id = Column(Integer, ForeignKey("sesiones_programadas.id"))
    estado = Column(String, default="activo")
    cliente = relationship("Cliente")
    sesion = relationship("SesionProgramada")