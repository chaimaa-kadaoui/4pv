import redis
from rest_framework import generics

from alerts.models import Alert
from alerts.serializers import AlertSerializer
from alerts.redis_manager import manager


class AlertList(generics.ListCreateAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer


class AlertDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer


class ActiveAlertDetail(generics.ListCreateAPIView):
    try:
        queryset = Alert.objects.filter(id__in=manager.get("active-alerts"))
    except TypeError:
        queryset = Alert.objects.none()
    serializer_class = AlertSerializer
