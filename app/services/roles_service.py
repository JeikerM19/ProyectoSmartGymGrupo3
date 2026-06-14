from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.rol import Rol
from app.services.base_service import CRUDBase
from app.core.exceptions import ReglaNegocioException  

class CRUDRol(CRUDBase[Rol]):

    async def crear(self, db: AsyncSession, *, obj_in: dict) -> Rol:
        nombre = obj_in.get("nombre")

        if nombre:
            stmt = select(Rol).where(Rol.nombre == nombre)
            result = await db.execute(stmt)
            rol_existente = result.scalars().first()

            if rol_existente:
                raise ReglaNegocioException(
                    codigo_interno="ERR_ROL_DUPLICADO",
                    mensaje=f"No se puede crear el rol: Ya existe un rol registrado con el nombre '{nombre}'."
                )

        return await super().crear(db, obj_in=obj_in)

rol = CRUDRol(Rol)  
rol_service = rol