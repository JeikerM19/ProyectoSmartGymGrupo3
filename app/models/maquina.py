from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Maquina(Base):
    __tablename__ = "maquinas"

    id = Column(Integer, primary_key = True)
    nombre = Column(String)
    descripcion = Column(String)
    estado = Column(String, default="activo")

    categoria_id = Column(Integer, ForeignKey("categorias_maquina.id"))

    categoria = relationship("CategoriaMaquina")