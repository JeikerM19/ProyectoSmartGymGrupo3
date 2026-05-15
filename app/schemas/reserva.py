from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ReservaBase(BaseModel):
    cliente_id: int
    sesion_id: int

class CrearReserva(ReservaBase):
    pass

class RespuestaReserva(ReservaBase):
    id: int
    fecha_reserva: datetime
    estado: str

    class Config:
        from_attributes = True