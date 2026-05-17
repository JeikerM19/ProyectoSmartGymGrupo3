from pydantic import BaseModel
from typing import Optional

class CategoriaBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None

class CrearCategoria(CategoriaBase):
    pass

class ActualizarCategoria(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None

class RespuestaCategoria(CategoriaBase):
    id: int
    estado: Optional[str] = None

    class Config:
        from_attributes = True