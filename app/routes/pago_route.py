from app.routes.crud_router import create_crud_router
from app.schemas.pago import CrearPago, ActualizarPago, RespuestaPago
from app.services.pago_service import Pago
from fastapi import Depends
from app.deps import RoleChecker

router = create_crud_router(
    prefix="/api/v1/pagos",
    service=Pago,
    create_schema=CrearPago,
    update_schema=ActualizarPago,
    read_schema=RespuestaPago,
    tag="Pagos",
    item_name="pago",
    activate=True,
    update_deps=[Depends(RoleChecker([4]))],
    create_deps=[Depends(RoleChecker([4,3]))],
    delete_deps=[Depends(RoleChecker([4]))],
    read_deps=[Depends(RoleChecker([4,1]))],
    obtein_deps=[Depends(RoleChecker([4,1]))]
)
