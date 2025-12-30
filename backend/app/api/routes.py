from fastapi import APIRouter

from app.services.exchange_service import ExchangeService
from app.calculations.averages import calculate_average
from app.core.config import load_settings
from app.calculations.ml_model import train_exchange_rate_model, predict_exchange_rate

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

@router.get("/ml_forecast")
def get_ml_forecast(year: int, month: int):
    model = train_exchange_rate_model()
    forecast = predict_exchange_rate(model, year, month)
    return {"forecast": forecast}

