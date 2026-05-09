from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Maquina(Base):
    __tablename__ = "maquinas"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    estado = Column(String, nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias_maquina.id"), nullable=False, index=True)

    categoria = relationship("CategoriaMaquina", back_populates="maquinas")
    tickets = relationship("TicketMantenimiento", back_populates="maquina")