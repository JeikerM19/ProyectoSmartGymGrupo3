from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class DetalleVentaSchema(BaseModel):
    producto_id: int
    cantidad: int
    precio_unitario: float

class CrearVenta(BaseModel):
    cliente_id: int
    detalles: List[DetalleVentaSchema]

class ActualizarVenta(BaseModel):
    cliente_id: Optional[int] = None
    detalles: Optional[List[DetalleVentaSchema]] = None
    total: Optional[float] = None
    fecha_venta: Optional[datetime] = None

class RespuestaVenta(BaseModel):
    id: int
    fecha_venta: datetime
    total: float
    cliente_id: int
    estado: Optional[str] = None

    class Config:
        from_attributes = True
