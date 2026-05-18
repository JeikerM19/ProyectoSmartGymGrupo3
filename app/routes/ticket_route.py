from app.routes.crud_router import create_crud_router
from app.schemas.ticket_mantenimiento import CrearTicket, ActualizarTicket, RespuestaTicket
from app.services.ticket_service import ticket_service

router = create_crud_router(
    prefix="/api/v1/tickets_mantenimiento",
    service=ticket_service,
    create_schema=CrearTicket,
    update_schema=ActualizarTicket,
    read_schema=RespuestaTicket,
    tag="Tickets Mantenimiento",
    item_name="ticket",
    activate=True,
)
