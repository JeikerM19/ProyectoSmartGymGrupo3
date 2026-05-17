from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    estado = Column(String, default="activo")
    rol_id = Column(Integer, ForeignKey("roles.id"))

    rol = relationship("Rol")