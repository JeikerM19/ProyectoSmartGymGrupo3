from datetime import datetime
from sqlalchemy import select, func, String, Integer, Float, Boolean, Date, DateTime
from typing import Any
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.services.base_service import CRUDBase
from app.models.ticket_mantenimiento import TicketMantenimiento
from app.models.usuario import Usuario
from app.models.maquina import Maquina
from datetime import date

class CRUDTicketMantenimiento(CRUDBase[TicketMantenimiento]):
    async def obtener_todos(self, db: AsyncSession, *, skip: int = 0, limit: int = 100) -> list[TicketMantenimiento]:
        result = await db.execute(
            select(TicketMantenimiento).options(joinedload(TicketMantenimiento.maquina)).offset(skip).limit(limit)
        )
        return result.scalars().all()

    async def obtener_paginado(self, db: AsyncSession, *, skip: int = 0, limit: int = 10, filters: dict | None = None):
        query = select(TicketMantenimiento).options(joinedload(TicketMantenimiento.maquina))

        if filters:
            for field, value in filters.items():
                if not hasattr(TicketMantenimiento, field):
                    continue

                column = getattr(TicketMantenimiento, field)

                try:
                    column_type = column.property.columns[0].type

                    if isinstance(column_type, String):
                        query = query.where(column.ilike(f"%{value}%"))

                    elif isinstance(column_type, Integer):
                        query = query.where(column == int(value))

                    elif isinstance(column_type, Float):
                        query = query.where(column == float(value))

                    elif isinstance(column_type, Boolean):
                        query = query.where(column == (str(value).lower() == "true"))

                    elif isinstance(column_type, Date):
                        query = query.where(column == date.fromisoformat(value))

                    elif isinstance(column_type, DateTime):
                        query = query.where(column == datetime.fromisoformat(value))

                    else:
                        query = query.where(column == value)

                except (ValueError, TypeError, AttributeError):
                    continue

        total_query = select(func.count()).select_from(query.subquery())

        total = await db.scalar(total_query)

        result = await db.execute(query.offset(skip).limit(limit))

        return {"total": total, "items": result.scalars().all()}


    async def obtener(self, db: AsyncSession, id: Any) -> TicketMantenimiento | None:
        result = await db.execute(
            select(TicketMantenimiento)
            .where(TicketMantenimiento.id == id)
            .options(joinedload(TicketMantenimiento.maquina))
        )
        return result.scalars().first()

    async def crear(self, db: AsyncSession, *, obj_in: dict) -> TicketMantenimiento:
        usuario_id = obj_in.get("usuario_id")
        usuario = await db.execute(select(Usuario).where(Usuario.id == usuario_id))
        usuario = usuario.scalars().first()
        if not usuario:
            raise HTTPException(status_code=404, detail="El usuario no existe.")
        maquina_id = obj_in.get("maquina_id")
        maquina = await db.execute(select(Maquina).where(Maquina.id == maquina_id))
        maquina = maquina.scalars().first()
        if not maquina:
            raise HTTPException(status_code=404, detail="La máquina no existe.")

        if maquina.estado == "mantenimiento":
            raise HTTPException(
                status_code=409, detail="La máquina ya se encuentra en mantenimiento."
            )

        maquina.estado = "mantenimiento"
        db.add(maquina)
        return await super().crear(db, obj_in=obj_in)

    async def cerrar_ticket(
        self, db: AsyncSession, *, ticket_id: int, costo: float
    ) -> TicketMantenimiento:

        ticket = await db.get(TicketMantenimiento, ticket_id)

        if not ticket:
            raise HTTPException(status_code=404, detail="El ticket no existe.")

        if ticket.fecha_cierre:
            raise HTTPException(status_code=409, detail="El ticket ya fue cerrado.")

        if costo < 0:
            raise HTTPException(
                status_code=400, detail="El costo no puede ser negativo."
            )
        ticket.costo = costo
        ticket.fecha_cierre = datetime.now()
        maquina = ticket.maquina
        maquina.estado = "activa"
        db.add(maquina)
        await db.commit()
        await db.refresh(ticket)
        return ticket

ticket_service = CRUDTicketMantenimiento(TicketMantenimiento)
