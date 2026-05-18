from app.routes.crud_router import create_crud_router
from app.schemas.venta_tienda import CrearVenta, ActualizarVenta, RespuestaVenta
from app.services.venta_service import venta_service

router = create_crud_router(
    prefix="/api/v1/ventas",
    service=venta_service,
    create_schema=CrearVenta,
    update_schema=ActualizarVenta,
    read_schema=RespuestaVenta,
    tag="Ventas",
    item_name="venta",
    activate=True,
)
