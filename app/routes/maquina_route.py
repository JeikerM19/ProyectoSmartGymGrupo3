from app.routes.crud_router import create_crud_router
from app.schemas.maquina import CrearMaquina, RespuestaMaquina, ActualizarMaquina
from app.schemas.estado import CambiarEstado
from app.services.maquina_service import maquina_service

router = create_crud_router(
    prefix="/api/v1/maquinas",
    service=maquina_service,
    create_schema=CrearMaquina,
    update_schema=ActualizarMaquina,
    read_schema=RespuestaMaquina,
    tag="Maquinas",
    item_name="máquina",
    state_schema=CambiarEstado,
)
