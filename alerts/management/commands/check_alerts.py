import json
from datetime import datetime
import redis
from django.core.management.base import BaseCommand

from alerts.models import Alert


r = redis.StrictRedis(host="localhost", port=6379, db=0)


def get_end_of_day():
    return datetime.now().replace(hour=23, minute=59, second=59).timestamp()


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("date", type=str)

    def handle(self, *args, **options):
        active_alerts = [alert.id for alert in Alert.objects.all() if alert.is_active(options["date"])]
        r.set("active-alerts", json.dumps(active_alerts))
        r.expireat("active-alerts", int(get_end_of_day()))
