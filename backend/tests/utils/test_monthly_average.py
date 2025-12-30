import pytest
from datetime import date
from app.db.models import ExchangeRate
from app.db.session import SessionLocal
from app.utils.monthly_average import compute_monthly_averages

@pytest.fixture
def seed_test_data():
    session = SessionLocal()
    session.query(ExchangeRate).delete()
    session.add_all([
        ExchangeRate(currency="USD", date=date(2023, 2, 1), rate=3.5),
        ExchangeRate(currency="USD", date=date(2023, 2, 28), rate=3.7),
        ExchangeRate(currency="USD", date=date(2023, 3, 1), rate=3.6),
        ExchangeRate(currency="USD", date=date(2023, 3, 31), rate=3.8),
    ])
    session.add_all([
        ExchangeRate(currency="EUR", date=date(2024, 2, 1), rate=4.0),
        ExchangeRate(currency="EUR", date=date(2024, 2, 29), rate=4.2),
    ])
    session.commit()
    yield
    session.query(ExchangeRate).delete()
    session.commit()
    session.close()

def test_monthly_average(seed_test_data):
    avg = compute_monthly_averages()
    assert avg["USD"]["2023-02"] == 3.6
    assert avg["USD"]["2023-03"] == 3.7
    assert avg["EUR"]["2024-02"] == 4.1
