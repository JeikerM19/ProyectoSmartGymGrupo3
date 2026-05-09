from fastapi import FastAPI
from contextlib import asynccontextmanager
import app.models
from app.db.base import Base
from app.db.session import engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(title="SmartGym API", lifespan=lifespan)

@app.get("/")
async def read_root():
    return {"message": "¡API de SmartGym funcionando perfectamente!"}