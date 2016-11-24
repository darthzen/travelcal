from django.db import models
from icalendar import Calendar,Event

class userCal(models.Model):
    traveler = models.CharField(max_length=40,primary_key=True)
# Create your models here.
