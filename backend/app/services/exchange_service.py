from datetime import date
import calendar

from app.clients.exchange_api import ExchangeApiClient

class ExchangeService:
    def __init__(self):
        self.client = ExchangeApiClient()

    def fetch_month_data(self, year: int, month: int) -> dict:
        last_day = calendar.monthrange(year, month)[1]

        start = date(year, month, 1)
        end = date(year, month, last_day)

        return self.client.get_monthly_rates(start, end)
