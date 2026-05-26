from pydantic import BaseModel, Field
from typing import Optional

class DisciplinaBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100)
    descripcion: Optional[str] = Field(None, max_length=255)

class CrearDisciplina(DisciplinaBase):
    pass

class ActualizarDisciplina(BaseModel):
    nombre: Optional[str] = Field(None, min_length=2, max_length=100)
    descripcion: Optional[str] = Field(None, max_length=255)

class RespuestaDisciplina(DisciplinaBase):
    id: int
    estado: str

    class Config:
        from_attributes = True
