from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import relationship
from app.db.base import Base

class TicketMantenimiento(Base):
    __tablename__ = "tickets_mantenimiento"

    id = Column(Integer, primary_key= True)
    descripcion = Column(String)
    fecha_apertura = Column(DateTime)
    fecha_cierre = Column(DateTime)
    costo = Column(Numeric)

    maquina_id = Column(Integer, ForeignKey("maquinas.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    maquina = relationship("Maquina")
    usuario = relationship("Usuario")