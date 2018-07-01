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


def check_condition(alert, date=None):
    date_field = DATE_FIELD[alert.data]
    if date is None:
        date = datetime.now().date()
    if not check_date(alert, date):
        print("{date} is out of alert {id}'s date range".format(date=date, id=alert.id))
        return

    data = read_data(alert, date_field)
    filtered_data = filter_data(data, alert, date_field)
    if len(filtered_data) == 0:
        print("Nothing to monitor")
        return

    if alert.condition == "smart":
        return get_smart_checks(alert)(data, filtered_data, date, date_field)
    return below_thresh(filtered_data, alert.data, alert.condition, date, date_field)



def check_date(alert, date):
    if isinstance(date, str):
        date = datetime.strptime(date, "%Y-%m-%d").date()
    return (alert.start_date <= date) and (alert.end_date >= date)


def read_data(alert, date_field):
    data = pd.read_csv(SOURCE_FILES[alert.data], parse_dates=[date_field])
    data = data.sort_values(by=date_field)
    return data


def filter_data(data, alert, date_field):
    # Filtering
    data = data[data[date_field] >= alert.start_date]
    data = data[data[date_field] <= alert.end_date]
    if alert.category is not None:
        data = data[data["category_id"] == alert.category]
    if alert.zone is not None:
        data = data[data["zone_id"] == alert.zone]
    return data


def below_thresh(df, value_field, thresh, date, date_field):
    actual_value = df.loc[df[date_field] == date, value_field].iat[0]
    return actual_value < float(thresh)


def get_thresh(df, date_field, value_field, date, method):
    # We don't take into account data from the "future"
    sub_df = df[df[date_field] <= date]
    thresh = getattr(sub_df[value_field], method)()  # either "mean" or "median"
    if method == "mean":
        thresh -= sub_df[value_field].std()
    return thresh


def smart_check_stocks(df, filtered_df, date, date_field):
    thresh = get_thresh(df, date_field, "available_resources", date, "median")
    print(thresh)
    return below_thresh(filtered_df, "available_resources", thresh, date, date_field)


def smart_check_price(df, filtered_df, date, date_field):
    thresh = get_thresh(df, date_field, "suggested_price", date, "mean")
    print(thresh)
    return below_thresh(filtered_df, "suggested_price", thresh, date, date_field)


def get_smart_checks(alert):
    return {
        "available_resources": smart_check_stocks,
        "suggested_price": smart_check_price,
    }[alert.data]
