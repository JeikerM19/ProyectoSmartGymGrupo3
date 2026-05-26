from pydantic import BaseModel, Field
from typing import Optional

class RolBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=50)

class CrearRol(RolBase):
    pass

class ActualizarRol(BaseModel):
    nombre: Optional[str] = Field(None, min_length=2, max_length=50)

class RespuestaRol(RolBase):
    id: int
    estado: str

    class Config:
        from_attributes = True
