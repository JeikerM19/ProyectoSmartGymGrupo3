from fastapi import FastAPI
from contextlib import asynccontextmanager
import app.models
from app.db.base import Base
from app.db.session import engine
from app.routes.maquina_route import router as maquina_router
from app.routes.categoria_route import router as categoria_router
from app.routes.cliente_route import router as cliente_router
from app.routes.control_route import router as control_router
from app.routes.disciplinas_route import router as disciplinas_router
from app.routes.entrenador_route import router as entrenador_router
from app.routes.evaluacion_route import router as evaluacion_router
from app.routes.membresia_route import router as membresia_router
from app.routes.rol_route import router as rol_router
from app.routes.pago_route import router as pago_router
from app.routes.plan_route import router as plan_router
from app.routes.producto_route import router as producto_router
from app.routes.reserva_route import router as reserva_router
from app.routes.sesion_route import router as sesion_router
from app.routes.usuario_route import router as usuario_router
from app.routes.venta_route import router as venta_router
from app.routes.ticket_route import router as ticket_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
    except Exception as exc:
        raise RuntimeError(
            "Error al conectar con la base de datos. Verifica que PostgreSQL esté en ejecución "
            "y que los datos de conexión en .env sean correctos."
        ) from exc
    yield

app = FastAPI(title="SmartGym API", lifespan=lifespan)

app.include_router(maquina_router)
app.include_router(categoria_router)
app.include_router(cliente_router)
app.include_router(control_router)
app.include_router(disciplinas_router)
app.include_router(entrenador_router)
app.include_router(evaluacion_router)
app.include_router(membresia_router)
app.include_router(rol_router)
app.include_router(pago_router)
app.include_router(plan_router)
app.include_router(producto_router)
app.include_router(reserva_router)
app.include_router(sesion_router)
app.include_router(usuario_router)
app.include_router(venta_router)
app.include_router(ticket_router)

@app.get("/")
async def read_root():
    return {"message": "¡API de SmartGym funcionando perfectamente!"}