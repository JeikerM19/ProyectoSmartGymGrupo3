from pydantic import BaseModel

class CambiarEstado(BaseModel):
    estado: str
