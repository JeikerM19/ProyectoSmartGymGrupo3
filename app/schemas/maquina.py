from pydantic import BaseModel
from typing import Optional

class MaquinaBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    estado: str
    categoria_id: int

class CrearMaquina(MaquinaBase):
    pass

class ActualizarMaquina(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    estado: Optional[str] = None
    categoria_id: Optional[int] = None

class RespuestaMaquina(MaquinaBase):
    id: int

    class Config:
        from_attributes = True
