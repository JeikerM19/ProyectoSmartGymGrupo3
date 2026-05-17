from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class ClienteBase(BaseModel):
    cedula: str
    nombre_completo: str
    email: EmailStr
    telefono: Optional[str] = None
    fecha_registro: date
    usuario_id: int

class CrearCliente(ClienteBase):
    pass

class ActualizarCliente(BaseModel):
    cedula: Optional[str] = None
    nombre_completo: Optional[str] = None
    email: Optional[EmailStr] = None
    telefono: Optional[str] = None
    fecha_registro: Optional[date] = None
    usuario_id: Optional[int] = None

class RespuestaCliente(ClienteBase):
    id: int
    estado: Optional[str] = None

    class Config:
        from_attributes = True
