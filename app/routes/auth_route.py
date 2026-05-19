from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel, EmailStr # Añadimos esto

from app.db.session import get_db
from app.security import verify_password, create_access_token 
from app.models.usuario import Usuario 

# Definimos el esquema para recibir JSON
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

router = APIRouter(prefix="/api/v1/auth", tags=["Auth"])

@router.post("/login")
async def login(
    credentials: LoginRequest, # Cambiamos form_data por nuestro esquema JSON
    db: AsyncSession = Depends(get_db)
):
    # 1. Buscar al usuario por su email. 
    # Ahora usamos credentials.email directamente del JSON
    result = await db.execute(select(Usuario).where(Usuario.email == credentials.email))
    user = result.scalars().first()

    # 2. Validar que el usuario exista y que la contraseña coincida
    if not user or not verify_password(credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # 3. Validar si el usuario está activo (aprovechando tu campo 'estado')
    if user.estado != "activo": 
        raise HTTPException(status_code=400, detail="Usuario inactivo")

    # 4. Construir el payload del token e incluir el rol
    access_token = create_access_token( 
        data={"sub": user.email, "role_id": user.rol_id} 
    )

    # 5. Devolver el JSON con el token
    return {"access_token": access_token, "token_type": "bearer"}