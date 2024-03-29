from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class HydroSystem(models.Model):
    """
    Model for a user's hydroponic system
    """
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Measurement(models.Model):
    """
    Model for a single measurement data from hydroponic system
    """
    system = models.ForeignKey(HydroSystem, on_delete=models.CASCADE)
    date = models.DateField()
    ph = models.FloatField()
    water_temperature = models.FloatField()
    tds = models.FloatField()