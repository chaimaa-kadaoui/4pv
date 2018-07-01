# Alert system

Create & manage alerts <br>
Instructions [here](INSTRUCTIONS.md) <br>
Using *python3*, *django* and *django REST framework*

## Usage

### Locally

* `pip3 install -r requirements.txt`
* [optional] Run `python3 manage.py create_alerts` to create the alerts described 
in [alert_config.py](alerts/management/commands/alert_config.py) or you can create your own alerts using the API after running the server <br>
* Run `python3 manage.py check_alerts` to check active alerts. 
You can also provide a specific date: `python3 manage.py check_alerts --date 2019-02-17`
* Run `python3 manage.py runserver` to launch the server. You can request the alerts API endpoints:
  * **GET** `host:port/alerts` to list all alerts
  * **GET/POST/PUT/DELETE** `host:port/alerts/[id]` to manage a specific alert
  * **GET** `host:port/alerts-active` to list all active alerts

### Using docker

* Build using docker `docker build -t alert-system .`
* Run the image providing the date of the checks `docker run -p 8000:8000 -d alert-system ./run.sh 2019-02-17` <br>
You can leave it blank for today `docker run -p 8000:8000 -d alert-system ./run.sh`
* Request the API to manage alerts

## Alert model

An alert has the following properties:
* `id` auto generated field
* `name` a unique name to describe the object
* `description` optional field to provide further detail
* `data` the data that should be monitored by the alert (4 types: *suggested_price*, *available_resources*, *yhat*, *error*)
* `start_date` and `end_date`
* condition
  * if condition is a number: the alert is active whenever the data is below this threshold
  * if condition = `"smart"`: apply custom monitoring, no threshold is provided
* optional: `zone` and `category` to filter datasets

### About "smart" mode

For now, basic rules are applied:
* For stocks: their value is constant throughout de days so we check if we are below the median or not
* For price: we check if the value is below the average minus the standard deviation
* For reco: same as price but each segment is treated separately; an alert is active if one check fails for each one of the segments

# TODO:
* analyze further the time series: extract repetition of patterns like weekends & period of the year
* add authentification
