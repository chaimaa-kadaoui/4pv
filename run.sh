echo $(date +"%Y-%m-%d") >> /var/log/cron.log 2>&1
echo $(date +"%T") Checking for active alerts >> /var/log/cron.log 2>&1
python3 /opt/alertsystem/manage.py check_alerts >> /var/log/cron.log 2>&1
echo $(date +"%T") Check finished >> /var/log/cron.log 2>&1
