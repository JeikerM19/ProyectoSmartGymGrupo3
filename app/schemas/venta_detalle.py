from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class DetalleVentaSchema(BaseModel):
    venta_id: int
    producto_id: int
    cantidad: int
    precio_unitario: float

class CrearVenta(BaseModel):
    venta_id: int
    producto_id: int
    cantidad: int
    precio_unitario: float

class ActualizarVenta(BaseModel):

    producto_id: Optional[int] = None
    cantidad: Optional[int] = None
    precio_unitario: Optional[float] = None

class RespuestaVenta(BaseModel):
    venta_id: int
    producto_id: int
    cantidad: int
    precio_unitario: float
    estado: Optional[str] = None

    class Config:
        from_attributes = True
