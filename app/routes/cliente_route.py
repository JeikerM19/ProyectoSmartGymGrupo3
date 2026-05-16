from app.routes.crud_router import create_crud_router
from app.schemas.categoria import ClienteCreate, ClienteUpdate, ClienteRead
from app.services.cliente_service import cliente_service

router = create_crud_router(
    prefix="/api/v1/cliente",
    service=cliente_service,
    create_schema=ClienteCreate,
    update_schema=ClienteUpdate,
    read_schema=ClienteRead,
    tag="Cliente",
    item_name="Cliente",
)
