from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ClienteRelacionResponse(BaseModel):
    id: int
    cedula: str  

    class Config:
        from_attributes = True


class ReservaBase(BaseModel):
    cliente_id: int
    sesion_id: int

class CrearReserva(ReservaBase):
    pass

class ActualizarReserva(BaseModel):
    cliente_id: Optional[int] = None
    sesion_id: Optional[int] = None
    estado: Optional[str] = None

class RespuestaReserva(ReservaBase):
    id: int
    fecha_reserva: datetime
    cliente: Optional[ClienteRelacionResponse] = None
    estado: str

    class Config:
        from_attributes = True
