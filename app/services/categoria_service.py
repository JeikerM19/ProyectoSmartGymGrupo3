from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.models.categoria_maquina import CategoriaMaquina
from app.services.base_service import CRUDBase


class CRUDCategoria(CRUDBase[CategoriaMaquina]):
    async def buscar_por_nombre(
        self, db: AsyncSession, nombre: str
    ) -> CategoriaMaquina | None:

        result = await db.execute(
            select(CategoriaMaquina).where(CategoriaMaquina.nombre == nombre)
        )

        return result.scalars().first()

    async def crear(self, db: AsyncSession, *, obj_in: dict) -> CategoriaMaquina:

        categoria = await self.buscar_por_nombre(db, obj_in["nombre"])

        if categoria:
            raise HTTPException(
                status_code=409, detail="Ya existe una categoría con ese nombre."
            )

        return await super().crear(db, obj_in=obj_in)

categoria_service = CRUDCategoria(CategoriaMaquina)
