from app.routes.crud_router import create_crud_router
from app.schemas.cliente import CrearCliente, ActualizarCliente, RespuestaCliente
from app.services.cliente_service import cliente_service

router = create_crud_router(
    prefix="/api/v1/cliente",
    service=cliente_service,
    create_schema=CrearCliente,
    update_schema=ActualizarCliente,
    read_schema=RespuestaCliente,
    tag="Cliente",
    item_name="Cliente",
    activate=True,
)
