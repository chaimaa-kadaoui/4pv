from django.core.management.base import BaseCommand

from alerts.models import Alert
from alerts.management.commands.alert_config import alerts


class Command(BaseCommand):

    def handle(self, *args, **options):
        if Alert.objects.count() > 0:
            print("Database not empty!")
            return
        for alert in alerts:
            Alert.objects.create(**alert)
