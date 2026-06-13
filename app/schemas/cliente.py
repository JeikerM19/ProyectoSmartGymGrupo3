from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

# --- NUEVO: Esquema para la información anidada del usuario ---
class UsuarioRelacionResponse(BaseModel):
    id: int
    nombre: str 
    email: str   

    class Config:
        from_attributes = True

class ClienteBase(BaseModel):
    cedula: str = Field(..., min_length=6, max_length=20)
    telefono: Optional[str] = Field(None, max_length=20)
    fecha_registro: date
    usuario_id: int

class CrearCliente(ClienteBase):
    pass

class ActualizarCliente(BaseModel):
    cedula: Optional[str] = Field(None, min_length=6, max_length=20)
    telefono: Optional[str] = Field(None, max_length=20)
    fecha_registro: Optional[date] = None
    usuario_id: Optional[int] = None

class RespuestaCliente(ClienteBase):
    usuario: Optional[UsuarioRelacionResponse] = None
    estado: str
    id: int
    # --- NUEVO: Agregamos la relación aquí ---
    

    class Config:
        from_attributes = True