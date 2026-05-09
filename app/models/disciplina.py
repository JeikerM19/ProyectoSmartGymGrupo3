from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Disciplina(Base):
    __tablename__ = "disciplinas"

    id = Column(Integer, primary_key = True)
    nombre = Column(String)
    descripcion = Column(String)