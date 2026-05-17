from app.routes.crud_router import create_crud_router
from app.schemas.evaluacion_biometrica import CrearEvaluacion, ActualizarEvaluacion, RespuestaEvaluacion
from app.services.evaluacion_service import evaluacion_service

router = create_crud_router(
    prefix="/api/v1/evaluaciones_biometricas",
    service=evaluacion_service,
    create_schema=CrearEvaluacion,
    update_schema=ActualizarEvaluacion,
    read_schema=RespuestaEvaluacion,
    tag="Evaluaciones Biometricas",
    item_name="evaluacion biometrica",
    activate=True,
)
