from app.routes.crud_router import create_crud_router
from app.schemas.venta_detalle import CrearDetalleVenta, ActualizarDetalleVenta, RespuestaDetalleVenta
from app.services.venta_detalle_service import detalle_venta_service
from fastapi import Depends
from app.core.deps import RoleChecker

router = create_crud_router(
    prefix="/api/v1/ventas_detalles",
    service=detalle_venta_service,
    create_schema=CrearDetalleVenta,
    update_schema=ActualizarDetalleVenta,
    read_schema=RespuestaDetalleVenta,
    tag="Ventas",
    item_name="venta",
    activate=True,
    update_deps=[Depends(RoleChecker([1,4]))],
    create_deps=[Depends(RoleChecker([1,4]))],
    delete_deps=[Depends(RoleChecker([4]))],
    read_deps=[Depends(RoleChecker([4]))],
    obtein_deps=[Depends(RoleChecker([4]))]
)
