DAY=$1

if [ -z "$1" ]; then
    DAY=$(date +"%Y-%m-%d")
else
    DAY=$1
fi

redis-server --daemonize yes
python3 manage.py check_alerts --date ${DAY}
python3 manage.py runserver 0.0.0.0:8000
