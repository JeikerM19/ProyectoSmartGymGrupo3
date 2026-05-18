from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Disciplina(Base):
    __tablename__ = "disciplinas"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False,unique=True)
    descripcion = Column(String,nullable=False)
    estado = Column(String, default="activo")
    sesiones = relationship("SesionProgramada", back_populates="disciplina")
