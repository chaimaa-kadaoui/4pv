base_alert = {
        "start_date": "2019-01-01",
        "end_date": "2019-03-01",
        "category": "PEL",
        "zone": "R320-Z001"
    }

base_name = "{data}-first-quarter-2019-PEL-R320-Z001-alert"

data_conditions = [
    ["suggested_price", "smart"],
    ["available_resources", "smart"],
    ["yhat", "smart"]
]

alerts = []
for to_monitor, condition in data_conditions:
    new_alert = base_alert.copy()  # No need for deepcopy
    new_alert.update({
        "name": base_name.format(data=to_monitor),
        "data": to_monitor,
        "condition": condition
    })
    alerts.append(new_alert)
