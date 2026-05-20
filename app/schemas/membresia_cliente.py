from pydantic import BaseModel
from datetime import date
from typing import Optional

class MembresiaBase(BaseModel):
    fecha_inicio: date
    fecha_vencimiento: date
    estado: str
    cliente_id: int
    plan_id: int

class CrearMembresia(MembresiaBase):
    pass

class ActualizarMembresia(BaseModel):
    fecha_inicio: Optional[date] = None
    fecha_vencimiento: Optional[date] = None
    cliente_id: Optional[int] = None
    plan_id: Optional[int] = None

class RespuestaMembresia(MembresiaBase):
    id: int

    class Config:
        from_attributes = True
