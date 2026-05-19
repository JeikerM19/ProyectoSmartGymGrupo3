from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class CategoriaMaquina(Base):
    __tablename__ = "categorias_maquina"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False, unique=True)
    descripcion = Column(String, nullable=True)
    estado = Column(String, default="activo")
    maquinas = relationship("Maquina", back_populates="categoria")
    
