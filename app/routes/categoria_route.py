from app.routes.crud_router import create_crud_router
from app.schemas.categoria import CategoriaCreate, CategoriaRead, CategoriaUpdate
from app.services.categoria_service import categoria_service

router = create_crud_router(
    prefix="/api/v1/categorias",
    service=categoria_service,
    create_schema=CategoriaCreate,
    update_schema=CategoriaUpdate,
    read_schema=CategoriaRead,
    tag="Categorias",
    item_name="categoría",
)
