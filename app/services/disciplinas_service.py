from app.models.disciplina import Disciplina
from app.services.base_service import CRUDBase

disciplina = CRUDBase(Disciplina) # Ni siquiera necesitas crear una clase si es un CRUD estándar
disciplina_service = disciplina