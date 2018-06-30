from datetime import datetime
import pandas as pd


SOURCE_FILES = {
    "suggested_price": "data/prices.csv",
    "yhat": "data/forecast.csv",
    "error": "data/forecast.csv",
    "available_resources": "data/stock.csv"
}


DATE_FIELD = {
    "suggested_price": "occupancy_date",
    "yhat": "occupancy_date",
    "error": "occupancy_date",
    "available_resources": "date"
}


def read_and_filter_data(alert):
    # Reading
    date_field = DATE_FIELD[alert.data]
    data = pd.read_csv(SOURCE_FILES[alert.data], parse_dates=[date_field])
    data = data.sort_values(by=date_field)

    # Filtering
    data = data[data[date_field] >= alert.start_date]
    data = data[data[date_field] <= alert.end_date]
    if alert.category is not None:
        data = data[data["category_id"] == alert.category]
    if alert.zone is not None:
        data = data[data["zone_id"] == alert.zone]

    return data


def check_date(alert, date):
    date = datetime.strptime(date, "%Y-%m-%d").date()
    return (alert.start_date <= date) and (alert.end_date >= date)


def check_condition(alert, date=None):
    date_field = DATE_FIELD[alert.data]
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    if not check_date(alert, date):
        print("{date} is out of alert {id}'s date range".format(date=date, id=alert.id))
        return
    data = read_and_filter_data(alert)
    if len(data) == 0:
        print("Nothing to monitor")
        return
    actual_value = data.loc[data[date_field] == date, alert.data].iat[0]
    return actual_value < float(alert.condition)
