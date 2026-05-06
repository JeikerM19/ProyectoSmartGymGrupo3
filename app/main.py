from fastapi import FastAPI
import app.models
from app.db.base import Base
from app.db.session import engine

app = FastAPI(title="SmartGym API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "¡API de SmartGym funcionando perfectamente!"}