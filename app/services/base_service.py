from typing import Generic, Type, TypeVar, List, Optional, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, String, Integer, Float, Boolean, Date, DateTime
from app.db.base import Base
from datetime import datetime, date

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

    async def obtener_paginado(self, db: AsyncSession, *, skip: int = 0, limit: int = 10, filters: dict | None = None):
        query = select(self.model)

        if filters:
            for field, value in filters.items():
                if not hasattr(self.model, field):
                    continue

                column = getattr(self.model, field)

                try:
                    column_type = column.property.columns[0].type

                    if isinstance(column_type, String):
                        query = query.where(column.ilike(f"%{value}%"))

                    elif isinstance(column_type, Integer):
                        query = query.where(column == int(value))

                    elif isinstance(column_type, Float):
                        query = query.where(column == float(value))

                    elif isinstance(column_type, Boolean):
                        query = query.where(column == (str(value).lower() == "true"))

                    elif isinstance(column_type, Date):
                        query = query.where(column == date.fromisoformat(value))

                    elif isinstance(column_type, DateTime):
                        query = query.where(column == datetime.fromisoformat(value))

                    else:
                        query = query.where(column == value)

                except (ValueError, TypeError, AttributeError):
                    continue

        total_query = select(func.count()).select_from(query.subquery())

        total = await db.scalar(total_query)

        result = await db.execute(query.offset(skip).limit(limit))

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
