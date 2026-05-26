from pydantic import BaseModel, Field
from typing import Optional

class PlanBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100)
    precio: float = Field(..., gt=0)
    duracion_dias: int = Field(..., gt=0)

class CrearPlan(PlanBase):
    pass

class ActualizarPlan(BaseModel):
    nombre: Optional[str] = Field(None, min_length=2, max_length=100)
    precio: Optional[float] = Field(None, gt=0)
    duracion_dias: Optional[int] = Field(None, gt=0)
    estado: Optional[str] = None

class RespuestaPlan(PlanBase):
    id: int
    estado: str

    class Config:
        from_attributes = True
