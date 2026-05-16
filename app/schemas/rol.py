from pydantic import BaseModel

class RolBase(BaseModel):
    nombre: str

class CrearRol(RolBase):
    pass

class RespuestaRol(RolBase):
    id: int

    class Config:
        from_attributes = True
