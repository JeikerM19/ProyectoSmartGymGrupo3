from pydantic import BaseModel, Field, model_validator
from datetime import date
from typing import Optional

class MembresiaBase(BaseModel):
    fecha_inicio: date
    fecha_vencimiento: date
    cliente_id: int
    plan_id: int
    estado: Optional[str] = "activo"

    @model_validator(mode="after")
    def validar_fechas(self):
        if self.fecha_vencimiento < self.fecha_inicio:
            raise ValueError(
                "La fecha_vencimiento debe ser mayor o igual a fecha_inicio"
            )

        return self

class CrearMembresia(MembresiaBase):
    pass

class ActualizarMembresia(BaseModel):
    fecha_inicio: Optional[date] = None
    fecha_vencimiento: Optional[date] = None
    cliente_id: Optional[int] = None
    plan_id: Optional[int] = None
    estado: Optional[str] = None

class RespuestaMembresia(MembresiaBase):
    id: int

    class Config:
        from_attributes = True
