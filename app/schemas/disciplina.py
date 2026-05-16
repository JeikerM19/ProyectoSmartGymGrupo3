from pydantic import BaseModel
from typing import Optional

class DisciplinaBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None

class CrearDisciplina(DisciplinaBase):
    pass

class RespuestaDisciplina(DisciplinaBase):
    id: int

    class Config:
        from_attributes = True