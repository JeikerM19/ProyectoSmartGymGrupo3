from sqlalchemy import Column, Integer, ForeignKey, Date, Time, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class SesionProgramada(Base):
    __tablename__ = "sesiones_programadas"

    id = Column(Integer, primary_key=True)
    fecha = Column(Date, nullable=False)
    hora_inicio = Column(Time, nullable=False)
    hora_fin = Column(Time, nullable=False)
    cupo_maximo = Column(Integer, nullable=False)
    disciplina_id = Column(Integer, ForeignKey("disciplinas.id"), nullable=False, index=True)
    entrenador_id = Column(Integer, ForeignKey("entrenadores.id"), nullable=False, index=True)
    estado = Column(String, default="activo")
    disciplina = relationship("Disciplina", back_populates="sesiones")
    entrenador = relationship("Entrenador", back_populates="sesiones")
    reservas = relationship("Reserva", back_populates="sesion")

