base_alert = {
        "start_date": "2019-01-01",
        "end_date": "2019-01-03",
        "category": "PEL",
        "zone": "R320-Z001"
    }

base_name = "{data}-first-quarter-2019-PEL-R320-Z001-alert"

data_threshs = [
    ["suggested_prices", 91.53],
    ["available_resources", 39]
]

alerts = []
for to_monitor, thresh in data_threshs:
    print(to_monitor)
    new_alert = base_alert.copy()  # No need for deepcopy
    new_alert.update({
        "name": base_name.format(data=to_monitor),
        "data": to_monitor,
        "condition": thresh
    })
    alerts.append(new_alert)
