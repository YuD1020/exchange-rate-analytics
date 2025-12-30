from sqlalchemy.orm import Session

from app.db.models import MonthlyExchangeRate

class ExchangeRepository:
    def __init__(self, session: Session):
        self.session = session

    def exists(self, year: int, month: int) -> bool:
        return (
            self.session.query(MonthlyExchangeRate)
            .filter_by(year=year, month=month)
            .first()
            is not None
        )

    def save(self, year: int, month: int, average: float) -> None:
        record = MonthlyExchangeRate(
            year=year,
            month=month,
            average_rate=average,
        )
        self.session.add(record)
