from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.services.base_service import CRUDBase
from app.models.membresia_cliente import MembresiaCliente
from app.models.plan_suscripcion import PlanSuscripcion
from app.models.cliente import Cliente

class CRUDDetalleVenta(CRUDBase[MembresiaCliente]):
    
    def create(self, db: Session, *, obj_in: dict) -> MembresiaCliente:
        # 1. Validar que el Plan de Suscripción existe
        plan_id = obj_in.get("plan_id")
        plan = db.query(PlanSuscripcion).filter(PlanSuscripcion.id == plan_id).first()
        if not plan:
            raise HTTPException(status_code=404, detail="No se puede crear la membresía: El plan de suscripción no existe.")

        # 2. Validar que el Cliente existe
        cliente_id = obj_in.get("cliente_id")
        cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
        if not cliente:
            raise HTTPException(status_code=404, detail="No se puede crear la membresía: El cliente no existe.")

        return super().create(db, obj_in=obj_in)