from typing import Any, List, Type, Optional
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from fastapi import params

def create_crud_router(
    prefix: str,
    service: Any,
    create_schema: Type[BaseModel],
    update_schema: Type[BaseModel],
    read_schema: Type[BaseModel],
    tag: str,
    item_name: str = "item",
    state_schema: Optional[Type[BaseModel]] = None,
    activate: bool = False,
    create_deps: Optional[list[params.Depends]] = None,
    update_deps: Optional[list[params.Depends]] = None,
    delete_deps: Optional[list[params.Depends]] = None,
    read_deps: Optional[list[params.Depends]] = None,
    obtein_deps: Optional[list[params.Depends]] = None,
) -> APIRouter:
    router = APIRouter(prefix=prefix, tags=[tag])

    @router.get("/", response_model=List[read_schema], dependencies=read_deps)
    async def leer_varios(db: AsyncSession = Depends(get_db)):
        return await service.obtener_todos(db)

    @router.get("/{item_id}", response_model=read_schema, dependencies=obtein_deps)
    async def leer(item_id: int, db: AsyncSession = Depends(get_db)):
        item = await service.obtener(db, item_id)
        if not item:
            raise HTTPException(status_code=404, detail=f"{item_name.capitalize()} no encontrado")
        return item

    @router.post("/", response_model=read_schema, dependencies=create_deps)
    async def crear(obj_in: create_schema, db: AsyncSession = Depends(get_db)):
        return await service.crear(db, obj_in=obj_in.model_dump(exclude_none=True))

    @router.put("/{item_id}", response_model=read_schema,dependencies=update_deps)
    async def actualizar(item_id: int, obj_in: update_schema, db: AsyncSession = Depends(get_db)):
        item = await service.obtener(db, item_id)
        if not item:
            raise HTTPException(status_code=404, detail=f"{item_name.capitalize()} no encontrado")
        return await service.actualizar(db, db_obj=item, obj_in=obj_in.model_dump(exclude_none=True))

    if state_schema is not None:
        @router.put("/{item_id}/estado", response_model=read_schema,dependencies=update_deps)
        async def cambiar_estado(item_id: int, obj_in: state_schema, db: AsyncSession = Depends(get_db)):
            item = await service.cambiar_estado(db, id=item_id, estado=obj_in.estado)
            if not item:
                raise HTTPException(status_code=404, detail=f"{item_name.capitalize()} no encontrado o no tiene campo estado")
            return item

    if activate:
        @router.put("/{item_id}/activar", response_model=read_schema,dependencies=update_deps)
        async def activar(item_id: int, db: AsyncSession = Depends(get_db)):
            item = await service.activar(db, id=item_id)
            if not item:
                raise HTTPException(status_code=400, detail=f"{item_name.capitalize()} no encontrado o no está en estado 'inactivo'")
            return item

    @router.delete("/{item_id}", dependencies=delete_deps)
    async def eliminar(item_id: int, db: AsyncSession = Depends(get_db)):
        deleted = await service.eliminacion_fisica(db, id=item_id)
        if not deleted:
            raise HTTPException(status_code=404, detail=f"{item_name.capitalize()} no encontrado")
        return {"detail": f"{item_name.capitalize()} eliminada"}

    @router.put("/{item_id}/desactivar", dependencies=update_deps)
    async def desactivar(item_id: int, db: AsyncSession = Depends(get_db)):
        obj = await service.eliminacion_logica(db, id=item_id)
        if not obj:
            raise HTTPException(status_code=404, detail=f"{item_name.capitalize()} no encontrado")
        return {"detail": f"{item_name.capitalize()} desactivada"}

    return router
