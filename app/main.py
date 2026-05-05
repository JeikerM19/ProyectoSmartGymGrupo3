from fastapi import FastAPI

app = FastAPI(title="SmartGym API")

@app.get("/")
def read_root():
    return {"message": "¡API de SmartGym funcionando perfectamente!"}