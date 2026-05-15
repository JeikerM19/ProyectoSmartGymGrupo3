from pydantic import BaseModel, EmailStr

class UsuarioBase(BaseModel):
    email: EmailStr
    rol_id: int

class CrearUsuario(UsuarioBase):
    password: str

class RespuestaUsuario(UsuarioBase):
    id: int

    class Config:
        from_attributes = True
