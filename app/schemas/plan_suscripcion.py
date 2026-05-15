from pydantic import BaseModel
from typing import Optional

class PlanBase(BaseModel):
    nombre: str
    precio: float
    duracion_dias: int

class CrearPlan(PlanBase):
    pass

class ActualizarPlan(BaseModel):
    nombre: Optional[str] = None
    precio: Optional[float] = None
    duracion_dias: Optional[int] = None

class RespuestaPlan(PlanBase):
    id: int

    class Config:
        from_attributes = True
