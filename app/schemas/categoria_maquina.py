from pydantic import BaseModel
from typing import Optional

class CategoriaBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None

class CrearCategoria(CategoriaBase):
    pass

class RespuestaCategoria(CategoriaBase):
    id: int

    class Config:
        from_attributes = True
