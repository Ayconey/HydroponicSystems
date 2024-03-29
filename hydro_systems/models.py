from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class HydroSystem(models.Model):
    """
    Model for a user's hydroponic system
    """
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200,null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_measurements(self):
        """
        returning all measurements from that system
        """
        return Measurement.objects.filter(system=self)


class Measurement(models.Model):
    """
    Model for a single measurement data from hydroponic system
    """
    system = models.ForeignKey(HydroSystem, on_delete=models.CASCADE)
    date = models.DateField()
    ph = models.FloatField()
    water_temperature = models.FloatField()
    tds = models.FloatField()