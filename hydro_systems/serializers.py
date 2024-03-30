from rest_framework import serializers
from .models import HydroSystem, Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    """
    Measurement data serializer, when creating on default sets system to one passed
    in url as pk
    """
    def __init__(self, *args, **kwargs):
        self.system = kwargs.pop('system', None)
        super().__init__(*args, **kwargs)

    def create(self, validated_data):
        validated_data['system'] = self.system
        return super().create(validated_data)

    class Meta:
        model = Measurement
        fields = ['id','date','ph','water_temperature','tds','system']
        read_only_fields = ['system']


class HydroSystemSerializer(serializers.ModelSerializer):
    """
    Hydroponic system serializer, when creating on default sets owner to
    current user, also with the system come 10 latest measurements
    """
    measurements = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def get_measurements(self, obj):
        measurements = obj.get_10_latest_measurements()
        return MeasurementSerializer(measurements, many=True).data

    def create(self, validated_data):
        validated_data['owner'] = self.request.user
        return super().create(validated_data)

    class Meta:
        model = HydroSystem
        fields = ['id', 'name','description','owner', 'measurements']
        read_only_fields = ['owner']