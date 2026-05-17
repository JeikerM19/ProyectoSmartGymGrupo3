from app.routes.crud_router import create_crud_router
from app.schemas.disciplina import CrearDisciplina, ActualizarDisciplina, RespuestaDisciplina
from app.services.disciplinas_service import disciplina_service

router = create_crud_router(
    prefix="/api/v1/disciplinas",
    service=disciplina_service,
    create_schema=CrearDisciplina,
    update_schema=ActualizarDisciplina,
    read_schema=RespuestaDisciplina,
    tag="Disciplinas",
    item_name="disciplina",
    activate=True,
)
