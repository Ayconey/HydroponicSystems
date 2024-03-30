from rest_framework import generics
from .serializers import HydroSystemSerializer, MeasurementSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status
from .models import HydroSystem, Measurement
from .permissions import IsOwner


# Hydroponic systems


class UserHydroSystemsListCreate(generics.ListCreateAPIView):
    """
    Api view of user's hydroponic systems.
    """
    serializer_class = HydroSystemSerializer

    def get_queryset(self):
        q = HydroSystem.objects.all().filter(owner=self.request.user)
        return q

    def post(self, request):
        # purpose of changing this function is to pass request info to serializer
        # in order to set owner = current logged user

        # passing request to serializer
        serializer = HydroSystemSerializer(data=request.data, request=request)

        # if everything is fine, pass data for further creation
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HydroSystemListCreate(generics.ListCreateAPIView):
    """
    Api view of all created hydroponic systems, only for admin.
    """
    permission_classes = [IsAdminUser]
    queryset = HydroSystem.objects.all()
    serializer_class = HydroSystemSerializer


class HydroSystemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Api view for managing hydroponic system which id is specified in url, with 10 latest
    measurements.
    """
    queryset = HydroSystem.objects.all()
    serializer_class = HydroSystemSerializer
    permission_classes = [IsOwner]


# Measurements


class MeasurementsFromHydroSystemListCreate(generics.ListCreateAPIView):
    """
    Api view for creating and showing all measurements for system which
    id is specified in url.
    """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        try:
            system = HydroSystem.objects.get(pk=pk)
        except HydroSystem.DoesNotExist:

            # # if system doesn't exists raise exception
            raise PermissionDenied("System with given ID does not exist.")

            # If owner != current user , raise permission denied exception
        if system.owner != self.request.user:
            raise PermissionDenied("You do not have permission to add measurement to this system.")
        return system.get_measurements()

    def post(self, request, pk=None):
        # when creating, set system to be the one specified in url
        system = HydroSystem.objects.get(pk=pk)

        # passing the system to serializer
        serializer = MeasurementSerializer(data=request.data, system=system)

        # if everything is fine, pass data for further creation
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeasurementRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Api view for managing single measurement specified in id
    """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = [IsOwner]
