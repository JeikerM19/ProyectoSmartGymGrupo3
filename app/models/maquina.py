from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Maquina(Base):
    __tablename__ = "maquinas"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, index=True)
    descripcion = Column(String(255), nullable=True)
    categoria_id = Column(Integer, ForeignKey("categorias_maquina.id"), nullable=False, index=True)
    estado = Column(String(20), nullable=False, default="activo")

    categoria = relationship("CategoriaMaquina", back_populates="maquinas")
    tickets = relationship("TicketMantenimiento", back_populates="maquina")
