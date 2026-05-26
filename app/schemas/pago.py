from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class PagoBase(BaseModel):
    monto: float = Field(..., gt=0)
    metodo_pago: str = Field(..., min_length=3, max_length=30)
    membresia_id: int

class CrearPago(PagoBase):
    pass

class ActualizarPago(BaseModel):
    monto: Optional[float] = Field(None, gt=0)
    metodo_pago: Optional[str] = Field(None, min_length=3, max_length=30)
    membresia_id: Optional[int] = None

class RespuestaPago(PagoBase):
    id: int
    fecha_pago: datetime
    estado: str

    class Config:
        from_attributes = True
