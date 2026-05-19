from app.models.disciplina import Disciplina
from app.services.base_service import CRUDBase

class CRUDDisciplina(CRUDBase[Disciplina]):
    pass

disciplina_service = CRUDDisciplina(Disciplina)