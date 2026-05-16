from pydantic import BaseModel
from typing import Optional

class ProductoBase(BaseModel):
    nombre: str
    precio: float
    stock: int

class CrearProducto(ProductoBase):
    pass

class ActualizarProducto(BaseModel):
    nombre: Optional[str] = None
    precio: Optional[float] = None
    stock: Optional[int] = None

class RespuestaProducto(ProductoBase):
    id: int

    class Config:
        from_attributes = True
