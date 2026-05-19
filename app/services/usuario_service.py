from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException
from app.services.base_service import CRUDBase
from app.models.usuario import Usuario
from app.models.rol import Rol


class CRUDUsuario(CRUDBase[Usuario]):
  
    async def crear(self, db: AsyncSession, *, obj_in: dict) -> Usuario:

        rol_id = obj_in.get("rol_id")
        result = await db.execute(select(Rol).filter(Rol.id == rol_id))
        rol = result.scalars().first()
        if not rol:
            raise HTTPException(status_code=404, detail="El rol especificado no existe.")

        return await super().crear(db, obj_in=obj_in)

usuario_service = CRUDUsuario(Usuario)
