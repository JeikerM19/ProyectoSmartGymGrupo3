from pydantic import BaseModel
from typing import Optional

class EntrenadorBase(BaseModel):
    especialidad: str
    usuario_id: int

class CrearEntrenador(EntrenadorBase):
    pass

class ActualizarEntrenador(BaseModel):
    especialidad: Optional[str] = None
    usuario_id: Optional[int] = None

class RespuestaEntrenador(EntrenadorBase):
    id: int
    estado: Optional[str] = None

    class Config:
        from_attributes = True
