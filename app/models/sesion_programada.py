from sqlalchemy import Column, Integer, ForeignKey, Date, Time, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class SesionProgramada(Base):
    __tablename__ = "sesiones_programadas"

    id = Column(Integer, primary_key=True)
    fecha = Column(Date)
    hora_inicio = Column(Time)
    hora_fin = Column(Time)
    cupo_maximo = Column(Integer)

    disciplina_id = Column(Integer, ForeignKey("disciplinas.id"))
    entrenador_id = Column(Integer, ForeignKey("entrenadores.id"))
    estado = Column(String, default="activo")
    disciplina = relationship("Disciplina")
    entrenador = relationship("Entrenador")