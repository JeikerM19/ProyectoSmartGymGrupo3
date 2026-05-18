from app.routes.crud_router import create_crud_router
from app.schemas.pago import CrearPago, ActualizarPago, RespuestaPago
from app.services.pago_service import pago

router = create_crud_router(
    prefix="/api/v1/pagos",
    service=pago,
    create_schema=CrearPago,
    update_schema=ActualizarPago,
    read_schema=RespuestaPago,
    tag="Pagos",
    item_name="pago",
    activate=True,
)
