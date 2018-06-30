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
    serializer_class = AlertSerializer

    def get_queryset(self):
        try:
            return Alert.objects.filter(id__in=manager.get("active-alerts"))
        except TypeError:
            return Alert.objects.none()
