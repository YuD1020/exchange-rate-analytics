from fastapi import FastAPI

from app.api.routes import router
from app.core.config import load_settings
from app.core.logging import setup_logging

settings = load_settings()
setup_logging(settings["log_level"])

app = FastAPI()
app.include_router(router)
