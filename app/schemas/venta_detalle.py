from pydantic import BaseModel, Field
from typing import Optional

class DetalleVentaBase(BaseModel):
    venta_id: int
    producto_id: int
    cantidad: int = Field(..., gt=0)
    precio_unitario: float = Field(..., gt=0)

class CrearDetalleVenta(DetalleVentaBase):
    pass

class ActualizarDetalleVenta(BaseModel):
    venta_id: Optional[int] = None
    producto_id: Optional[int] = None
    cantidad: Optional[int] = Field(None, gt=0)
    precio_unitario: Optional[float] = Field(None, gt=0)
    estado: Optional[str] = None

class RespuestaDetalleVenta(DetalleVentaBase):
    id: int
    estado: str

    class Config:
        from_attributes = True
