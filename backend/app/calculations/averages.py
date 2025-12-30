def calculate_average(rates: dict) -> float:
    values = []

    for day in rates.get("rates", {}).values():
        values.extend(day.values())

    if not values:
        raise ValueError("No exchange rate data available")

    return sum(values) / len(values)
