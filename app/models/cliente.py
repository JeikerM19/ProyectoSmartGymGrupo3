from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True)
    cedula = Column(String, unique=True)
    telefono = Column(String)
    estado = Column(String, default="activo")
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    usuario = relationship("Usuario")