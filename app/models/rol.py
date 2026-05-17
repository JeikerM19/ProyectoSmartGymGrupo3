from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Rol(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    estado = Column(String, default="activo")