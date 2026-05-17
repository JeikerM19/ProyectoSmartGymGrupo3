from pydantic import BaseModel
from datetime import date
from typing import Optional

class EvaluacionBase(BaseModel):
    fecha: date
    peso: float
    estatura: float
    porcentaje_grasa: Optional[float] = None
    observaciones: Optional[str] = None
    cliente_id: int

class CrearEvaluacion(EvaluacionBase):
    pass

class ActualizarEvaluacion(BaseModel):
    fecha: Optional[date] = None
    peso: Optional[float] = None
    estatura: Optional[float] = None
    porcentaje_grasa: Optional[float] = None
    observaciones: Optional[str] = None
    cliente_id: Optional[int] = None

class RespuestaEvaluacion(EvaluacionBase):
    id: int
    estado: Optional[str] = None

    class Config:
        from_attributes = True
