from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.services.base_service import CRUDBase
from app.models.reserva import Reserva
from app.models.cliente import Cliente
from app.models.sesion_programada import SesionProgramada # O el nombre de tu tabla de horarios

class CRUDReserva(CRUDBase[Reserva]):
    
    def create(self, db: Session, *, obj_in: dict) -> Reserva:
        # 1. Validar que el Cliente existe
        cliente_id = obj_in.get("cliente_id")
        cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
        if not cliente:
            raise HTTPException(status_code=404, detail="No se puede reservar: El cliente no existe.")

        # 2. Validar que la Clase o Sesión existe
        sesion_id = obj_in.get("sesion_id")
        sesion = db.query(SesionProgramada).filter(SesionProgramada.id == sesion_id).first()
        if not sesion:
            raise HTTPException(status_code=404, detail="No se puede reservar: La sesión no existe.")

        # 3. Validación de Negocio Opcional: ¿Hay cupos disponibles?
        # if sesion.cupos_disponibles <= 0:
        #    raise HTTPException(status_code=400, detail="La sesión ya está llena.")

        # 4. Integración con el motor genérico
        # Usamos super().create para que se encargue del db.add y db.commit
        return super().create(db, obj_in=obj_in)

    def cancelar_reserva(self, db: Session, reserva_id: int):
        return self.remove_logical(db, id=reserva_id)

# Instancia lista para usar en tus rutas de FastAPI
reserva_service = CRUDReserva(Reserva)