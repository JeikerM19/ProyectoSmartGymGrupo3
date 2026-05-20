from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

class CrearDetalleVenta(BaseModel):
    producto_id: int
    cantidad: int
    precio_unitario: float

class CrearVenta(BaseModel):
    cliente_id: int
    detalles: List[CrearDetalleVenta] = Field(..., min_length=1)
    total: float
    fecha_venta: datetime


class ActualizarVenta(BaseModel):
    cliente_id: Optional[int] = None
    total: Optional[float] = None
    fecha_venta: Optional[datetime] = None

class RespuestaVenta(BaseModel):
    id: int
    total: float
    cliente_id: int
    fecha_venta: datetime
    estado: Optional[str] = None

    class Config:
        from_attributes = True
