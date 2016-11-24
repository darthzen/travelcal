from django.db import models

class Trip(models.Model):
    bcd_locator = models.CharField(max_length=10,primary_key=True)
    traveler_firstname = models.CharField(max_length=30)
    traveler_lastname = models.CharField(max_length=30)
    air_locator = models.CharField(max_length=10)

class Flights(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
