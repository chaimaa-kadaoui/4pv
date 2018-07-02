from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from alerts.analysis import check_condition
from alerts.redis_manager import manager

MAX_LENGTH = 120

MONITORED = (
    ("suggested_price", "Prix suggéré"),
    ("yhat", "Prévision"),
    ("error", "Erreur"),
    ("available_resources", "Stock disponible"),
)


class Alert(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=MAX_LENGTH, unique=True)
    description = models.TextField(null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    data = models.CharField(max_length=MAX_LENGTH, choices=MONITORED)
    zone = models.CharField(max_length=MAX_LENGTH, null=True)
    category = models.CharField(max_length=MAX_LENGTH, null=True)
    condition = models.CharField(max_length=10)

    def is_active(self, date):
        return check_condition(self, date)


@receiver(pre_delete)
def delete_from_active(sender, instance, **kwargs):
    # When an alert is removed, checks if it is stored as active in Redis
    if sender == Alert:
        active = manager.get("active-alerts")
        if instance.id in active:
            active.remove(instance.id)
            manager.set("active-alerts", active)
