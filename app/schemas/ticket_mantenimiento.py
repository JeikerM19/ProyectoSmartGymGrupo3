from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TicketBase(BaseModel):
    descripcion: str
    maquina_id: int

class CrearTicket(TicketBase):
    pass

class CerrarTicket(BaseModel):
    costo: float

class RespuestaTicket(TicketBase):
    id: int
    fecha_apertura: datetime
    fecha_cierre: Optional[datetime] = None
    costo: Optional[float] = None

    class Config:
        from_attributes = True
