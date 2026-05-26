from pydantic import BaseModel, Field

class CambiarEstado(BaseModel):
    estado: str = Field(..., min_length=3, max_length=20)
