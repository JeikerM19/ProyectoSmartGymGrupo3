from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.db.base import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True)
    cedula = Column(String(20), unique=True, nullable=False, index=True)
    telefono = Column(String(20), nullable=True)
    fecha_registro = Column(Date, nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False, unique=True, index=True)
    estado = Column(String(20), default="activo", nullable=False)

    usuario = relationship("Usuario", back_populates="cliente", lazy="joined")
    reservas = relationship("Reserva", back_populates="cliente")
    membresias = relationship("MembresiaCliente", back_populates="cliente")
    evaluaciones = relationship("EvaluacionBiometrica", back_populates="cliente")
    accesos = relationship("ControlAcceso", back_populates="cliente")
    ventas = relationship("VentaTienda", back_populates="cliente")
