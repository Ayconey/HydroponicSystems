from rest_framework import generics
from .models import HydroSystem, Measurement
from .serializers import HydroSystemSerializer, MeasurementSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
# Hydroponic systems


class UserHydroSystemsListCreate(generics.ListCreateAPIView):
    """
    Api view of user's hydroponic systems
    """
    serializer_class = HydroSystemSerializer

    def get_queryset(self):
        q = HydroSystem.objects.all().filter(owner=self.request.user)
        return q

    def post(self, request):
        # purpouse of changing this function is to pass request info to serializer
        # in order to set owner = current logged user

        serializer = HydroSystemSerializer(data=request.data, request=request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HydroSystemListCreate(generics.ListCreateAPIView):
    """
    Api view of all created hydroponic systems, only for admin
    """
    permission_classes = [IsAdminUser]
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
