from app.routes.crud_router import create_crud_router
from app.schemas.sesion_programada import CrearSesion, ActualizarSesion, RespuestaSesion
from app.services.sesion_service import sesion_service

router = create_crud_router(
    prefix="/api/v1/sesiones",
    service=sesion_service,
    create_schema=CrearSesion,
    update_schema=ActualizarSesion,
    read_schema=RespuestaSesion,
    tag="Sesiones",
    item_name="sesion",
    activate=True,
)
