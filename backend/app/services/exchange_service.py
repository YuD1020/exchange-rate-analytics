from datetime import date

from app.clients.exchange_api import ExchangeApiClient

class ExchangeService:
    def __init__(self):
        self.client = ExchangeApiClient()

    def fetch_month_data(self, year: int, month: int) -> dict:
        start = date(year, month, 1)
        end = date(year, month, 28)

        return self.client.get_monthly_rates(start, end)
