from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.session import get_db
from app.core.security import verify_password, create_access_token
from app.models.usuario import Usuario
from app.schemas.login import LoginRequest

router = APIRouter(prefix="/api/v1/auth", tags=["Auth"])

@router.post("/login")
async def login(credentials: LoginRequest, db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(Usuario).where(Usuario.email == credentials.email))

    user = result.scalars().first()

    if not user or not verify_password(credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if user.estado != "activo":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario inactivo"
        )

    access_token = create_access_token(data={"sub": user.email, "role_id": user.rol_id})

    return {"access_token": access_token, "token_type": "bearer"}
