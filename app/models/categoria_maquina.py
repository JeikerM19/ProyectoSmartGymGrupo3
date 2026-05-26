from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class CategoriaMaquina(Base):
    __tablename__ = "categorias_maquina"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True, index=True)
    descripcion = Column(String(255), nullable=True)
    estado = Column(String(20), default="activo", nullable=False)
    maquinas = relationship("Maquina", back_populates="categoria")
