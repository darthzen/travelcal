from django.db import models
from icalendar import Calendar,Event
from travelcal import Trip

def userCal(models.Model):
    traveler = models.CharField(max_length=40,primary_key=True)
# Create your models here.
