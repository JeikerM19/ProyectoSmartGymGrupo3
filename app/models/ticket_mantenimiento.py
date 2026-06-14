from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric, CheckConstraint
from sqlalchemy.orm import relationship
from app.db.base import Base

class TicketMantenimiento(Base):
    __tablename__ = "tickets_mantenimiento"
    __table_args__ = (CheckConstraint("costo >= 0", name="check_costo_ticket"),)

    id = Column(Integer, primary_key=True)
    descripcion = Column(String(255), nullable=False)
    fecha_apertura = Column(DateTime, nullable=False)
    fecha_cierre = Column(DateTime, nullable=True)
    costo = Column(Numeric(10, 2), nullable=True)
    maquina_id = Column(Integer, ForeignKey("maquinas.id"), nullable=False, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False, index=True)
    estado = Column(String(20), default="activo", nullable=False)

    maquina = relationship("Maquina", back_populates="tickets", lazy="joined")
    usuario = relationship("Usuario", back_populates="tickets_mantenimiento", lazy="joined")
