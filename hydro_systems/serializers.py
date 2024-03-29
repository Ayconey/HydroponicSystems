from rest_framework import serializers
from .models import HydroSystem, Measurement


class HydroSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HydroSystem
        fields = '__all__'


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'
