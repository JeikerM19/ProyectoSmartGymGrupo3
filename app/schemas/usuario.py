from pydantic import BaseModel, EmailStr
from typing import Optional

class UsuarioBase(BaseModel):
    email: EmailStr
    rol_id: int

class CrearUsuario(UsuarioBase):
    password: str

class ActualizarUsuario(BaseModel):
    email: Optional[EmailStr] = None
    rol_id: Optional[int] = None
    password: Optional[str] = None

class RespuestaUsuario(UsuarioBase):
    id: int
    estado: Optional[str] = None

    class Config:
        from_attributes = True
