from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.models.disciplina import Disciplina
from app.services.base_service import CRUDBase

class CRUDDisciplina(CRUDBase[Disciplina]):
    async def buscar_por_nombre(
        self, db: AsyncSession, nombre: str
    ) -> Disciplina | None:

        result = await db.execute(select(Disciplina).where(Disciplina.nombre == nombre))

        return result.scalars().first()

    async def crear(self, db: AsyncSession, *, obj_in: dict) -> Disciplina:

        disciplina = await self.buscar_por_nombre(db, obj_in["nombre"])

        if disciplina:
            raise HTTPException(
                status_code=409, detail="Ya existe una disciplina con ese nombre."
            )

        return await super().crear(db, obj_in=obj_in)

disciplina_service = CRUDDisciplina(Disciplina)
