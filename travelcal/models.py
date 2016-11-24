from django.db import models

class Traveler(models.Model):
    traveler = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)

class Trip(models.Model):
    bcd_locator = models.CharField(max_length=10,primary_key=True)
    traveler = models.ForeignKey(Traveler, on_delete=models.CASCADE)
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
    day_out = models.DateTimeField()
