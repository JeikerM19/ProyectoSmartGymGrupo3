from app.routes.crud_router import create_crud_router
from app.schemas.categoria_maquina import CrearCategoria, RespuestaCategoria, ActualizarCategoria
from app.services.categoria_service import categoria_service

router = create_crud_router(
    prefix="/api/v1/categorias",
    service=categoria_service,
    create_schema=CrearCategoria,
    update_schema=ActualizarCategoria,
    read_schema=RespuestaCategoria,
    tag="Categorias",
    item_name="categoría",
    activate=True,
)
