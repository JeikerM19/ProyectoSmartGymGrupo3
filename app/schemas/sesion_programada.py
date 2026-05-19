from pydantic import BaseModel
from datetime import date, time
from typing import Optional

class SesionBase(BaseModel):
    fecha: date
    hora_inicio: time
    hora_fin: time
    cupo_maximo: int
    disciplina_id: int
    entrenador_id: int
    estado: Optional[str] = "activo"

class CrearSesion(SesionBase):
    pass

class ActualizarSesion(BaseModel):
    fecha: Optional[date] = None
    hora_inicio: Optional[time] = None
    hora_fin: Optional[time] = None
    cupo_maximo: Optional[int] = None
    disciplina_id: Optional[int] = None
    entrenador_id: Optional[int] = None
    estado: Optional[str] = None

class RespuestaSesion(SesionBase):
    id: int

    class Config:
        from_attributes = True
