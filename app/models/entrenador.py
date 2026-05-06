from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Entrenador(Base):
    __tablename__ = "entrenadores"

    id = Column(Integer, primary_key = True)
    especialidad = Column(String)

    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    usuario = relationship("Usuario")

