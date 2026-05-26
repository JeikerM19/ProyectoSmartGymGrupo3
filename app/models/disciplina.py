from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Disciplina(Base):
    __tablename__ = "disciplinas"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True, index=True)
    descripcion = Column(String(255), nullable=True)
    estado = Column(String(20), default="activo", nullable=False)

    sesiones = relationship("SesionProgramada", back_populates="disciplina")
