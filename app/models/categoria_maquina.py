from sqlalchemy import Column, Integer, String
from app.db.base import Base

class CategoriaMaquina(Base):
    __tablename__ = "categorias_maquina"

    id = Column(Integer, primary_key = True)
    nombre = Column(String, nullable = False)
    estado = Column(String, default="activo")