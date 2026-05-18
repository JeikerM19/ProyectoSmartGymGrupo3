from app.routes.crud_router import create_crud_router
from app.schemas.reserva import CrearReserva, ActualizarReserva, RespuestaReserva
from app.services.reserva_service import reserva_service

router = create_crud_router(
    prefix="/api/v1/reservas",
    service=reserva_service,
    create_schema=CrearReserva,
    update_schema=ActualizarReserva,
    read_schema=RespuestaReserva,
    tag="Reservas",
    item_name="reserva",
    activate=True,
)
