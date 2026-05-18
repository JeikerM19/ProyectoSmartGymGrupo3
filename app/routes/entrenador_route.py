from app.routes.crud_router import create_crud_router
from app.schemas.entrenador import CrearEntrenador, ActualizarEntrenador, RespuestaEntrenador
from app.services.entrenador_service import entrenador_service

router = create_crud_router(
    prefix="/api/v1/entrenadores",
    service=entrenador_service,
    create_schema=CrearEntrenador,
    update_schema=ActualizarEntrenador,
    read_schema=RespuestaEntrenador,
    tag="Entrenadores",
    item_name="entrenador",
    activate=True,
)
