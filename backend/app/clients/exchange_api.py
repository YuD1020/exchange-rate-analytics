import requests
from datetime import date

class ExchangeApiError(RuntimeError):
    pass

class ExchangeApiClient:
    BASE_URL = "https://api.frankfurter.app"

    def get_monthly_rates(self, start: date, end: date) -> dict:
        url = f"{self.BASE_URL}/{start}..{end}"
        params = {"from": "USD", "to": "ILS"}

        response = requests.get(url, params=params, timeout=10)
        if response.status_code != 200:
            raise ExchangeApiError("Failed to fetch exchange rates")

        return response.json()
