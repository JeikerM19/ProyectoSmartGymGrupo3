from sqlalchemy import Column, Integer, ForeignKey, Numeric, DateTime, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Pago(Base):
    __tablename__ = "pagos"

    id = Column(Integer, primary_key=True)
    monto = Column(Numeric)
    fecha_pago = Column(DateTime)
    metodo_pago = Column(String)

    membresia_id = Column(Integer, ForeignKey("membresias_cliente.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    estado = Column(String, default="activo")
    membresia = relationship("MembresiaCliente")
    usuario = relationship("Usuario")