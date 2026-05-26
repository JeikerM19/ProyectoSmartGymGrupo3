from pydantic import BaseModel, Field
from typing import Optional

class EntrenadorBase(BaseModel):
    especialidad: str = Field(..., min_length=3, max_length=100)
    usuario_id: int

class CrearEntrenador(EntrenadorBase):
    pass

class ActualizarEntrenador(BaseModel):
    especialidad: Optional[str] = Field(None, min_length=3, max_length=100)
    usuario_id: Optional[int] = None

class RespuestaEntrenador(EntrenadorBase):
    id: int
    estado: str

    class Config:
        from_attributes = True
