from pydantic import BaseModel
from datetime import datetime

class CrearControlAcceso(BaseModel):
    cedula: str

class RespuestaControlAcceso(BaseModel):
    id: int
    cliente_id: int
    fecha_hora: datetime
    mensaje: str

    class Config:
        from_attributes = True
