from fastapi import FastAPI
from app.config.settings import load_settings

settings = load_settings()

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok", "env": settings["env"]}
