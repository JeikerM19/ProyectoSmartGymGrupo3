from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TicketBase(BaseModel):
    descripcion: str
    maquina_id: int

class CrearTicket(TicketBase):
    pass

class ActualizarTicket(BaseModel):
    descripcion: Optional[str] = None
    maquina_id: Optional[int] = None
    fecha_cierre: Optional[datetime] = None
    costo: Optional[float] = None

class CerrarTicket(BaseModel):
    costo: float

class RespuestaTicket(TicketBase):
    id: int
    fecha_apertura: datetime
    fecha_cierre: Optional[datetime] = None
    costo: Optional[float] = None
    estado: Optional[str] = None

    class Config:
        from_attributes = True
