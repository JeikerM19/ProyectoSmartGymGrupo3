from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ControlAccesoBase(BaseModel):
    cedula: str

class CrearControlAcceso(ControlAccesoBase):
    pass

class ActualizarControlAcceso(BaseModel):
    cedula: Optional[str] = None

class RespuestaControlAcceso(BaseModel):
    id: int
    cliente_id: int
    fecha_hora: datetime
    mensaje: str
    estado: Optional[str] = None

    class Config:
        from_attributes = True
