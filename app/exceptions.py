from fastapi import status
from datetime import datetime

class ReglaNegocioException(Exception):
    """
    Excepción personalizada para capturar fallos en las reglas de negocio
    del gimnasio (SmartGym). Retorna automáticamente un código 409 Conflict.
    """
    def __init__(self, codigo_interno: str, mensaje: str):
        self.status_code = status.HTTP_409_CONFLICT
        self.error = "Conflict"
        self.codigo_interno = codigo_interno
        self.mensaje = mensaje
        # Formato de fecha ISO estricto con la Z al final
        self.timestamp = datetime.utcnow().isoformat() + "Z"