from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Entrenador(Base):
    __tablename__ = "entrenadores"

    id = Column(Integer, primary_key=True)
    especialidad = Column(String(100), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False, unique=True, index=True)
    estado = Column(String(20), default="activo", nullable=False)

    usuario = relationship("Usuario", back_populates="entrenador", lazy="joined")
    sesiones = relationship("SesionProgramada", back_populates="entrenador")
