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

class RespuestaEvaluacion(EvaluacionBase):
    id: int

    class Config:
        from_attributes = True
