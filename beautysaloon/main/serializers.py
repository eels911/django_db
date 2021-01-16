from rest_framework import serializers

from .models import Visits


class VisitsSerializer(serializers.Serializer):
    visit_number = serializers.CharField(max_length=80)
    service_name = serializers.CharField(max_length=70)
    fio_client = serializers.CharField(max_length=60)
    fio_staff = serializers.CharField(max_length=60)
    price = serializers.IntegerField()

    def create(self, validated_data):
        return Visits.objects.create(**validated_data)
