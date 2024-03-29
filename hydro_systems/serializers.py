from rest_framework import serializers
from .models import HydroSystem, Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'


class HydroSystemSerializer(serializers.ModelSerializer):
    measurements = serializers.SerializerMethodField()  # Dodano pole "measurements"

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = HydroSystem
        fields = ['id', 'name','description','owner', 'measurements']
        read_only_fields = ['owner']

    def get_measurements(self, obj):
        measurements = obj.get_measurements()
        return MeasurementSerializer(measurements, many=True).data

    def create(self, validated_data):
        validated_data['owner'] = self.request.user
        return super().create(validated_data)