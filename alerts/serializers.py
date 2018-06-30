from rest_framework import serializers

from alerts.models import Alert


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ('id', 'name', 'description', 'data', 'monitored_data', 'start_date', 'end_date', 'zone', 'category', 'segment')
        extra_kwargs = {
            'data': {'write_only': True},
            'monitored_data': {'source': 'get_data_display', 'read_only': True},
            'zone': {'required': False},
            'category': {'required': False},
            'segment': {'required': False},
        }
