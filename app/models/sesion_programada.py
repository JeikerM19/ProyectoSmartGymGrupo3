from sqlalchemy import Column, Integer, ForeignKey, Date, Time, String, CheckConstraint
from sqlalchemy.orm import relationship
from app.db.base import Base

class SesionProgramada(Base):
    __tablename__ = "sesiones_programadas"
    __table_args__ = (CheckConstraint("hora_fin > hora_inicio", name="check_horario_valido"),)

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    fecha = Column(Date, nullable=False)
    hora_inicio = Column(Time, nullable=False)
    hora_fin = Column(Time, nullable=False)
    cupo_maximo = Column(Integer, nullable=False)
    disciplina_id = Column(Integer, ForeignKey("disciplinas.id"), nullable=False, index=True)
    entrenador_id = Column(Integer, ForeignKey("entrenadores.id"), nullable=False, index=True)
    estado = Column(String(20), default="activo", nullable=False)

    disciplina = relationship("Disciplina", back_populates="sesiones")
    entrenador = relationship("Entrenador", back_populates="sesiones")
    reservas = relationship("Reserva", back_populates="sesion")
