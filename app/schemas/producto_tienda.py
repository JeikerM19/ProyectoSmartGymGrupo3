from pydantic import BaseModel, Field
from typing import Optional

class ProductoBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100)
    precio: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)

class CrearProducto(ProductoBase):
    pass

class ActualizarProducto(BaseModel):
    nombre: Optional[str] = Field(None, min_length=2, max_length=100)
    precio: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)

class RespuestaProducto(ProductoBase):
    id: int
    estado: str

    class Config:
        from_attributes = True
