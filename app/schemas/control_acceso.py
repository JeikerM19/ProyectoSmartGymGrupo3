from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ControlAccesoBase(BaseModel):
    cliente_id: int
    fecha_hora: datetime
    mensaje: Optional[str]

class CrearControlAcceso(ControlAccesoBase):
    cliente_id: int
    fecha_hora: datetime
    mensaje: Optional[str] = None

class ActualizarControlAcceso(BaseModel):
    cliente_id: Optional[int] = None
    fecha_hora: Optional[datetime] = None
    mensaje: Optional[str] = None

class RespuestaControlAcceso(BaseModel):
    id: int
    cliente_id: int
    fecha_hora: datetime
    mensaje: str
    estado: Optional[str] = None

    class Config:
        from_attributes = True
