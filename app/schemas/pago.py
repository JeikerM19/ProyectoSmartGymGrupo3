from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PagoBase(BaseModel):
    monto: float
    metodo_pago: str
    membresia_id: int

class CrearPago(PagoBase):
    pass

class ActualizarPago(BaseModel):
    monto: Optional[float] = None
    metodo_pago: Optional[str] = None
    membresia_id: Optional[int] = None
    fecha_pago: Optional[datetime] = None

class RespuestaPago(PagoBase):
    id: int
    fecha_pago: datetime
    estado: Optional[str] = None

    class Config:
        from_attributes = True
