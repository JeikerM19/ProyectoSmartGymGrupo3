from pydantic import BaseModel
from typing import Optional

class RolBase(BaseModel):
    nombre: str
    estado: Optional[str] = "activo"

class CrearRol(RolBase):
    pass

class ActualizarRol(BaseModel):
    nombre: Optional[str] = None

class RespuestaRol(RolBase):
    id: int

    class Config:
        from_attributes = True
