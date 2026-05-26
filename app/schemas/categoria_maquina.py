from pydantic import BaseModel, Field
from typing import Optional

class CategoriaBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100)
    descripcion: Optional[str] = Field(None, max_length=255)

class CrearCategoria(CategoriaBase):
    pass

class ActualizarCategoria(BaseModel):
    nombre: Optional[str] = Field(None, min_length=2, max_length=100)
    descripcion: Optional[str] = Field(None, max_length=255)

class RespuestaCategoria(CategoriaBase):
    id: int
    estado: str

    class Config:
        from_attributes = True
