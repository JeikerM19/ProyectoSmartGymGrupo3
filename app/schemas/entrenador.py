from pydantic import BaseModel

class EntrenadorBase(BaseModel):
    especialidad: str
    usuario_id: int

class CrearEntrenador(EntrenadorBase):
    pass

class RespuestaEntrenador(EntrenadorBase):
    id: int

    class Config:
        from_attributes = True
