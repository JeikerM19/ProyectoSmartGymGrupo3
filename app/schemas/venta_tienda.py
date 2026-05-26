from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

class CrearDetalleVenta(BaseModel):
    producto_id: int
    cantidad: int = Field(..., gt=0)
    precio_unitario: float = Field(..., gt=0)

class VentaBase(BaseModel):
    cliente_id: int
    total: float = Field(..., ge=0)

class CrearVenta(VentaBase):
    detalles: List[CrearDetalleVenta] = Field(..., min_length=1)

class ActualizarVenta(BaseModel):
    cliente_id: Optional[int] = None
    total: Optional[float] = Field(None, ge=0)
    estado: Optional[str] = None

class RespuestaVenta(VentaBase):
    id: int
    fecha_venta: datetime
    estado: str

    class Config:
        from_attributes = True
