from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import load_settings

settings = load_settings()

engine = create_engine(
    settings["database_url"],
    future=True,
    echo=False,
)

SessionLocal = sessionmaker(bind=engine, autoflush=False)
