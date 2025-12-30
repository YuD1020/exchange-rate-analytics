from datetime import date
from sqlalchemy.orm import Session

from app.db.init_db import init_db
from app.db.session import SessionLocal
from app.repositories.exchange_repository import ExchangeRepository
from app.services.exchange_service import ExchangeService
from app.calculations.averages import calculate_average

START_YEAR = 2023
START_MONTH = 1

def seed() -> None:
    init_db()
    today = date.today()
    service = ExchangeService()

    session: Session = SessionLocal()
    repo = ExchangeRepository(session)

    try:
        year, month = START_YEAR, START_MONTH

        while (year, month) <= (today.year, today.month):
            if not repo.exists(year, month):
                data = service.fetch_month_data(year, month)
                average = calculate_average(data)
                repo.save(year, month, average)

            if month == 12:
                year += 1
                month = 1
            else:
                month += 1

        session.commit()

    finally:
        session.close()


if __name__ == "__main__":
    seed()
