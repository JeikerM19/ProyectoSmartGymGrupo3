from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ReservaBase(BaseModel):
    cliente_id: int
    sesion_id: int

class CrearReserva(ReservaBase):
    pass

class ActualizarReserva(BaseModel):
    cliente_id: Optional[int] = None
    sesion_id: Optional[int] = None

class RespuestaReserva(ReservaBase):
    id: int
    fecha_reserva: datetime
    estado: str

    class Config:
        from_attributes = True