from datetime import datetime
from collections import defaultdict

from app.db.models import ExchangeRate
from app.db.session import SessionLocal

def compute_monthly_averages():
    session = SessionLocal()
    try:
        rates = session.query(ExchangeRate).all()
        monthly_data = defaultdict(list)

        for rate in rates:
            month_key = rate.date.strftime("%Y-%m")  # YYYY-MM
            monthly_data[(rate.currency, month_key)].append(rate.rate)

        monthly_avg = {}
        for (currency, month), values in monthly_data.items():
            avg = sum(values) / len(values)
            if currency not in monthly_avg:
                monthly_avg[currency] = {}
            monthly_avg[currency][month] = round(avg, 4)
        
        return monthly_avg
    finally:
        session.close()
