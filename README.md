# SmartGym API

API en FastAPI + PostgreSQL para gestión de usuarios, roles y máquinas de gimnasio.

---

## Instalación y ejecución

```bash
git clone <URL_DEL_REPOSITORIO>
cd lab1-proyecto
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

Configurar .env
Crear la base de datos

$env:PYTHONPATH = "."
.\.venv\Scripts\python.exe scripts/seed.py

uvicorn app.main:app --reload

Login colocar los datos del seed
Colocar el token para obtener la autorizacion