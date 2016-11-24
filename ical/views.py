from datetime import datetime
from icalendar import Calendar, Event
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request,employee):
    trips = travelcal.Traveler.objects.get(traveler = employee).Trip()
    cal = Calendar()
    for trip in trips:
        ical_event = Event()
        ical_event.add('summary','')
        ical_event.add('dtstart','')
        ical_event.add('dtend','')
        ical_event.add('dtstamp','')
        cal.add_component(ical_event)
    response = HttpResponse(cal.as_string(), mimetype="text/calendar")
    response['Content-Disposition'] = 'attachment; filename=%s.ics' % employee.slug
    return response
