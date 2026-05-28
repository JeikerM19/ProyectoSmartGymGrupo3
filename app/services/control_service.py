from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from app.services.base_service import CRUDBase
from app.models.control_acceso import ControlAcceso
from app.models.cliente import Cliente
from app.schemas.control_acceso import CrearControlAcceso
from app.models.membresia_cliente import MembresiaCliente
from datetime import date

class CRUDControlAcceso(CRUDBase[ControlAcceso]):
    async def crear(self, db: AsyncSession, *, obj_in: dict) -> ControlAcceso:
        # Extraemos el cliente_id directamente del diccionario
        cliente_id = obj_in.get("cliente_id")

        if not cliente_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El campo 'cliente_id' es obligatorio."
            )

        # 1. Buscar la membresía más reciente de este cliente
        stmt = (
            select(MembresiaCliente)
            .where(MembresiaCliente.cliente_id == cliente_id)
            .order_by(MembresiaCliente.fecha_vencimiento.desc())
        )
        result = await db.execute(stmt)
        membresia = result.scalars().first()

        # 2. Validación: ¿El cliente tiene alguna membresía registrada?
        if not membresia:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Acceso denegado: El cliente no posee ninguna membresía registrada."
            )

        # 3. Validación de la Regla de Negocio (Estado y Fecha de Vencimiento)
        hoy = date.today()
        
        if membresia.estado.lower() != "activo":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Acceso denegado: La membresía se encuentra en estado '{membresia.estado}'."
            )
            
        if membresia.fecha_vencimiento < hoy:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Acceso denegado: La membresía expiró el {membresia.fecha_vencimiento}."
            )

        # 4. Construimos el objeto final usando los datos que venían en obj_in 
        # e inyectamos el mensaje automatizado
        db_obj = ControlAcceso(
            cliente_id=cliente_id,
            mensaje=f"Acceso permitido - Membresía válida hasta {membresia.fecha_vencimiento}",
            estado="activo"
        )
        
        # 5. Guardamos en la base de datos
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        
        return db_obj

control_acceso_service = CRUDControlAcceso(ControlAcceso)
