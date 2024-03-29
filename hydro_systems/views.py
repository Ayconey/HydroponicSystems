from rest_framework import generics
from .models import HydroSystem, Measurement
from .serializers import HydroSystemSerializer, MeasurementSerializer

# Hydroponic systems


class HydroSystemListCreate(generics.ListCreateAPIView):
    queryset = HydroSystem.objects.all()
    serializer_class = HydroSystemSerializer


class HydroSystemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = HydroSystem.objects.all()
    serializer_class = HydroSystemSerializer

# Measurements


class MeasurementListCreate(generics.ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class MeasurementRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
