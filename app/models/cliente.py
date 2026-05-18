from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True)
    cedula = Column(String, unique=True, nullable=False)
    nombre_completo = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False, unique=True)

    usuario = relationship("Usuario",back_populates="cliente")
    reservas = relationship("Reserva", back_populates="cliente")
    membresias = relationship("MembresiaCliente", back_populates="cliente")
    evaluaciones = relationship("EvaluacionBiometrica",back_populates="cliente")
    accesos = relationship("ControlAcceso", back_populates="cliente")
    ventas = relationship("VentaTienda", back_populates="cliente")
    estado = Column(String, default="activo")
