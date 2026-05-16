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

class RespuestaCliente(ClienteBase):
    id: int

    class Config:
        from_attributes = True
