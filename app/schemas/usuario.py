from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UsuarioBase(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    rol_id: int

class CrearUsuario(UsuarioBase):
    password: str = Field(..., min_length=8, max_length=100)

class ActualizarUsuario(BaseModel):
    nombre: Optional[str] = Field(None, min_length=3, max_length=100)
    email: Optional[EmailStr] = None
    rol_id: Optional[int] = None
    password: Optional[str] = Field(None, min_length=8, max_length=100)


class RespuestaUsuario(UsuarioBase):
    id: int
    estado: str

    class Config:
        from_attributes = True
