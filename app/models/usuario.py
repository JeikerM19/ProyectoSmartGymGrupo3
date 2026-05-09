from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    rol_id = Column(Integer, ForeignKey("roles.id"), nullable=False, index=True)

    rol = relationship("Rol", back_populates="usuarios")
    cliente = relationship("Cliente", back_populates="usuario", uselist=False)
    entrenador = relationship("Entrenador", back_populates="usuario", uselist=False)
    pagos = relationship("Pago", back_populates="usuario")
    tickets_mantenimiento = relationship("TicketMantenimiento", back_populates="usuario")