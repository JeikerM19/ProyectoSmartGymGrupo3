from pydantic import BaseModel
from typing import Optional

class DisciplinaBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None

class CrearDisciplina(DisciplinaBase):
    pass

class ActualizarDisciplina(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None

class RespuestaDisciplina(DisciplinaBase):
    id: int
    estado: Optional[str] = None

    class Config:
        from_attributes = True