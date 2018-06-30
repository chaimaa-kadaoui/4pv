from django.db import models

from alerts.analysis import check_condition

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
