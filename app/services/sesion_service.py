from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.services.base_service import CRUDBase
from app.models.sesion_programada import SesionProgramada
from app.models.entrenador import Entrenador
from app.models.disciplina import Disciplina

class CRUDSesion(CRUDBase[SesionProgramada]):

    async def obtener_por_entrenador(self, db: Session, entrenador_id: int):
        return db.query(self.model).filter(
            self.model.entrenador_id == entrenador_id,
            self.model.estado != "cancelada"
        ).all()
        
    async def crear(self, db: Session, *, obj_in: dict) -> SesionProgramada:

        entrenador_id = obj_in.get("entrenador_id")
        entrenador = db.query(Entrenador).filter(Entrenador.id == entrenador_id).first()
        if not entrenador:
            raise HTTPException(status_code=404, detail="El entrenador especificado no existe.")

        disciplina_id = obj_in.get("disciplina_id")
        disciplina = db.query(Disciplina).filter(Disciplina.id == disciplina_id).first()
        if not disciplina:
            raise HTTPException(status_code=404, detail="La disciplina especificada no existe.")

        return super().create(db, obj_in=obj_in)

sesion_service = CRUDSesion(SesionProgramada)