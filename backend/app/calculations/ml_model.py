import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from app.db.session import SessionLocal
from app.db.models import ExchangeRate

def train_exchange_rate_model():
    session = SessionLocal()
    rates = session.query(ExchangeRate).all()
    data = []

    for rate in rates:
        data.append({"date": rate.date, "rate": rate.rate})

    df = pd.DataFrame(data)
    df['month'] = pd.to_datetime(df['date']).dt.month
    df['year'] = pd.to_datetime(df['date']).dt.year

    X = df[['year', 'month']]
    y = df['rate']

    model = LinearRegression()
    model.fit(X, y)

    return model

def predict_exchange_rate(model, year: int, month: int):
    return model.predict([[year, month]])[0]
