from fastapi import APIRouter
from app.core.config import load_settings

router = APIRouter()
settings = load_settings()

@router.get("/health")
def health():
    return {
        "status": "ok",
        "env": settings["env"]
    }
