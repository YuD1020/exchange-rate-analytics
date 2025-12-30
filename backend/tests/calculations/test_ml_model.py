from app.calculations.ml_model import train_exchange_rate_model, predict_exchange_rate

def test_ml_model():
    model = train_exchange_rate_model()
    forecast = predict_exchange_rate(model, 2023, 12)
    assert forecast is not None
    assert isinstance(forecast, float)
