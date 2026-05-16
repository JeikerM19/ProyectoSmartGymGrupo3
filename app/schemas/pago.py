from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PagoBase(BaseModel):
    monto: float
    metodo_pago: str
    membresia_id: int

class CrearPago(PagoBase):
    pass

class RespuestaPago(PagoBase):
    id: int
    fecha_pago: datetime

    class Config:
        from_attributes = True
