from app.routes.crud_router import create_crud_router
from app.schemas.usuario import CrearUsuario, ActualizarUsuario, RespuestaUsuario
from app.services.usuario_service import usuario_service

router = create_crud_router(
    prefix="/api/v1/usuarios",
    service=usuario_service,
    create_schema=CrearUsuario,
    update_schema=ActualizarUsuario,
    read_schema=RespuestaUsuario,
    tag="Usuarios",
    item_name="usuario",
    activate=True,
)
