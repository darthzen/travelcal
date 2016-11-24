from django.db import models

class Trip(models.Model):
    bcd_locator = models.CharField(max_length=10,primary_key=True)
    traveler = models.CharField(max_length=40)
    air_locator = models.CharField(max_length=10)

class Flights(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    airline = models.CharField(max_length=40)
    flight = models.CharField(max_length=10)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()

class Rentals(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    agency = models.CharField(max_length=30)
    date_in = models.DateTimeField()
    day_out = models.DateTimeField()

class Hotels(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    date_in = models.DateTimeField()
    day_out = models.DateTimeField(l
