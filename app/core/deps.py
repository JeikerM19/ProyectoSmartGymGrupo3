from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer # Cambiamos a HTTPBearer
from app.core.security import decode_token

# 1. Este cambio es la clave: HTTPBearer activa el cuadro de "Value" en Swagger
# Ya no te pedirá username ni password.
security_scheme = HTTPBearer()

class RoleChecker:
    def __init__(self, allowed_roles_ids: list[int]):
        self.allowed_roles_ids = allowed_roles_ids

    # 2. Ahora la dependencia recibe el objeto 'token' de HTTPBearer
    async def __call__(self, token: str = Depends(security_scheme)):
        # Extraemos el string del token de las credenciales
        payload = decode_token(token.credentials)
        print(payload)
        
        if not payload:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Token inválido o expirado"
            )
        
        # 3. Verificamos el rol (Admin=1, Entrenador=2, etc.)
        user_role_id = payload.get("role_id")
        
        if user_role_id not in self.allowed_roles_ids:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, 
                detail="No tienes los permisos necesarios para esta acción"
            )
        
        return payload