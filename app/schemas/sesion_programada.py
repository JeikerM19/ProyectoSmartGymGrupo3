from pydantic import BaseModel, Field, model_validator
from datetime import date, time
from typing import Optional

class EntrenadorRelacionResponse(BaseModel):
    id: int
    especialidad: str


class SesionBase(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=100)
    fecha: date
    hora_inicio: time
    hora_fin: time
    cupo_maximo: int = Field(..., gt=0)
    disciplina_id: int
    entrenador_id: int
    estado: Optional[str] = "activo"

    @model_validator(mode="after")
    def validar_horario(self):
        if self.hora_fin <= self.hora_inicio:
            raise ValueError("La hora_fin debe ser mayor que hora_inicio")

        return self

class CrearSesion(SesionBase):
    pass

class ActualizarSesion(BaseModel):
    nombre: Optional[str] = Field(None, min_length=3, max_length=100)
    fecha: Optional[date] = None
    hora_inicio: Optional[time] = None
    hora_fin: Optional[time] = None
    cupo_maximo: Optional[int] = Field(None, gt=0)
    disciplina_id: Optional[int] = None
    entrenador_id: Optional[int] = None
    estado: Optional[str] = None

class RespuestaSesion(SesionBase):
    id: int
    entrenador: Optional[EntrenadorRelacionResponse] = None
    class Config:
        from_attributes = True
