from datetime import datetime
from django.core.management.base import BaseCommand

from alerts.models import Alert
from alerts.redis_manager import manager
from alerts.logging import logger


def get_end_of_day():
    return datetime.now().replace(hour=23, minute=59, second=59).timestamp()


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("--date", type=str)

    def handle(self, *args, **options):
        active_alerts = [alert.id for alert in Alert.objects.all() if alert.is_active(options.get("date"))]
        logger.info("Alerts check: {cnt} alert(s) active today".format(cnt=len(active_alerts)))
        manager.set("active-alerts", active_alerts, expire_at=get_end_of_day())
