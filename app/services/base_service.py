from typing import Generic, Type, TypeVar, List, Optional, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.db.base import Base

# Definimos un tipo genérico que debe ser un modelo de SQLAlchemy
ModelType = TypeVar("ModelType", bound=Base)


class CRUDBase(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def obtener(self, db: AsyncSession, id: Any) -> Optional[ModelType]:
        return await db.get(self.model, id)

    async def obtener_todos(
        self, db: AsyncSession, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        result = await db.execute(select(self.model).offset(skip).limit(limit))
        return result.scalars().all()

    async def obtener_paginado(
        self, db: AsyncSession, *, skip: int = 0, limit: int = 10
    ):
        total = await db.scalar(select(func.count()).select_from(self.model))
        result = await db.execute(select(self.model).offset(skip).limit(limit))
        return {"total": total, "items": result.scalars().all()}

    async def crear(self, db: AsyncSession, *, obj_in: dict) -> ModelType:
        db_obj = self.model(**obj_in)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def actualizar(
        self, db: AsyncSession, *, db_obj: ModelType, obj_in: dict
    ) -> ModelType:
        for field in obj_in:
            if hasattr(db_obj, field):
                setattr(db_obj, field, obj_in[field])
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def cambiar_estado(
        self, db: AsyncSession, *, id: Any, estado: str
    ) -> Optional[ModelType]:
        obj = await db.get(self.model, id)
        if obj and hasattr(obj, "estado"):
            obj.estado = estado
            await db.commit()
            await db.refresh(obj)
            return obj
        return None

    # --- ELIMINACIONES ---

    async def eliminacion_logica(
        self, db: AsyncSession, *, id: int
    ) -> Optional[ModelType]:
        obj = await db.get(self.model, id)
        if obj and hasattr(obj, "estado"):
            obj.estado = "inactivo"
            await db.commit()
            await db.refresh(obj)
        return obj

    async def activar(self, db: AsyncSession, *, id: Any) -> Optional[ModelType]:
        obj = await db.get(self.model, id)
        if obj and hasattr(obj, "estado") and getattr(obj, "estado") == "inactivo":
            obj.estado = "activo"
            await db.commit()
            await db.refresh(obj)
            return obj
        return None

    async def eliminacion_fisica(self, db: AsyncSession, *, id: int) -> bool:
        obj = await db.get(self.model, id)
        if obj:
            await db.delete(obj)
            await db.commit()
            return True
        return False
