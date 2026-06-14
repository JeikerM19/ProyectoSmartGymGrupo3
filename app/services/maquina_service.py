from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.base_service import CRUDBase
from app.models.maquina import Maquina
from app.models.categoria_maquina import CategoriaMaquina  
from app.core.exceptions import ReglaNegocioException  

class CRUDMaquina(CRUDBase[Maquina]):
    
    async def crear(self, db: AsyncSession, *, obj_in: dict) -> Maquina:

        categoria_id = obj_in.get("categoria_id") 

        if categoria_id:
            stmt_categoria = select(CategoriaMaquina).where(CategoriaMaquina.id == categoria_id)
            result_categoria = await db.execute(stmt_categoria)
            categoria_existente = result_categoria.scalars().first()

            if not categoria_existente:
                raise ReglaNegocioException(
                    codigo_interno="ERR_CATEGORIA_NO_ENCONTRADA",
                    mensaje=f"No se puede registrar la máquina: La categoría con ID {categoria_id} no existe."
                )
        else:
            raise ReglaNegocioException(
                codigo_interno="ERR_CATEGORIA_REQUERIDA",
                mensaje="El campo 'categoria_id' es obligatorio para registrar una máquina."
            )

        return await super().crear(db, obj_in=obj_in)
    
maquina_service = CRUDMaquina(Maquina)