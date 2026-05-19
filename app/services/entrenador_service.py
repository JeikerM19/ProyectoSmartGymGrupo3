from app.models.entrenador import Entrenador
from app.services.base_service import CRUDBase

class CRUDEntrenador(CRUDBase[Entrenador]):
    async def buscar_por_disciplina(self, db, disciplina: str):
        return db.query(self.model).filter(self.model.disciplina == disciplina).first()

entrenador = CRUDEntrenador(Entrenador)
entrenador_service = entrenador