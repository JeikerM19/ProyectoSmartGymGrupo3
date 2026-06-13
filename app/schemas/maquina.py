from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class EstadoMaquina(str, Enum):
    ACTIVO = "activo"
    MANTENIMIENTO = "mantenimiento"
    INACTIVO = "inactivo"

class MaquinaBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100)
    descripcion: Optional[str] = Field(None, max_length=255)
    categoria_id: int

class CrearMaquina(MaquinaBase):
    pass

class ActualizarMaquina(BaseModel):
    nombre: Optional[str] = Field(None, min_length=2, max_length=100)
    descripcion: Optional[str] = Field(None, max_length=255)
    categoria_id: Optional[int] = None
    estado: Optional[EstadoMaquina] = None

class RespuestaMaquina(MaquinaBase):
    id: int
    estado: EstadoMaquina

    class Config:
        from_attributes = True
