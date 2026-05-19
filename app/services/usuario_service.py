from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.services.base_service import CRUDBase
from app.models.usuario import Usuario
from app.models.rol import Rol


class CRUDUsuario(CRUDBase[Usuario]):
  
    async def crear(self, db: Session, *, obj_in: dict) -> Usuario:

        rol_id = obj_in.get("rol_id")
        rol = db.query(Rol).filter(Rol.id == rol_id).first()
        if not rol:
            raise HTTPException(status_code=404, detail="El rol especificado no existe.")

        return super().create(db, obj_in=obj_in)

usuario_service = CRUDUsuario(Usuario)
