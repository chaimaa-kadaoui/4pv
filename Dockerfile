# Setup
FROM redis

RUN mkdir -p /opt/alertsystem
WORKDIR /opt/alertsystem
COPY . /opt/alertsystem

# Python3
RUN apt-get update && apt-get install -y curl python3 cron
RUN cd /tmp \
    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python3 get-pip.py

RUN pip3 install -r requirements.txt

# Init
RUN python3 manage.py migrate
RUN python3 manage.py makemigrations alerts
RUN python3 manage.py migrate
RUN python3 manage.py create_alerts

# Expose port
EXPOSE 8000

## Crons
ADD scripts/crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab
RUN touch /var/log/cron.log
RUN /usr/bin/crontab /etc/cron.d/crontab
