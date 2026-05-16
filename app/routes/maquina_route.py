from app.routes.crud_router import create_crud_router
from app.schemas.maquina import MaquinaCreate, MaquinaRead, MaquinaUpdate
from app.services.maquina_service import maquina_service

router = create_crud_router(
    prefix="/api/v1/maquinas",
    service=maquina_service,
    create_schema=MaquinaCreate,
    update_schema=MaquinaUpdate,
    read_schema=MaquinaRead,
    tag="Maquinas",
    item_name="máquina",
)
