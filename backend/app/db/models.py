from sqlalchemy import Integer, Float, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base

class MonthlyExchangeRate(Base):
    __tablename__ = "monthly_exchange_rates"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    year: Mapped[int]
    month: Mapped[int]
    average_rate: Mapped[float]

    __table_args__ = (
        UniqueConstraint("year", "month", name="uq_year_month"),
    )
