from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Rol(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), unique=True, nullable=False, index=True)
    estado = Column(String(20), default="activo", nullable=False)

    usuarios = relationship("Usuario", back_populates="rol")
