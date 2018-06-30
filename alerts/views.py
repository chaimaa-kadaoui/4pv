from rest_framework import generics

from alerts.models import Alert
from alerts.serializers import AlertSerializer

class AlertList(generics.ListCreateAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer


class AlertDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
