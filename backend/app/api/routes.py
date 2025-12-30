from fastapi import APIRouter

from app.services.exchange_service import ExchangeService
from app.calculations.averages import calculate_average
from app.core.config import load_settings

router = APIRouter()
settings = load_settings()

@router.get("/health")
def health():
    return {
        "status": "ok",
        "env": settings["env"]
    }

@router.get("/average")
def get_monthly_average(year: int, month: int):
    exchange_service = ExchangeService()
    rates = exchange_service.fetch_month_data(year, month)
    average = calculate_average(rates)
    return {"average": average}
