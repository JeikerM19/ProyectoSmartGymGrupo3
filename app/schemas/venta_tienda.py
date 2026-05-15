from pydantic import BaseModel
from datetime import datetime
from typing import List

class DetalleVentaSchema(BaseModel):
    producto_id: int
    cantidad: int
    precio_unitario: float

class CrearVenta(BaseModel):
    cliente_id: int
    detalles: List[DetalleVentaSchema]

class RespuestaVenta(BaseModel):
    id: int
    fecha_venta: datetime
    total: float
    cliente_id: int

    class Config:
        from_attributes = True
