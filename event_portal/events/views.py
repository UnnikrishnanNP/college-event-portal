from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def home(request):
    event = Event.objects.all()
    event_status = EventStatus.objects.all()
    ongoing_events = event_status.filter(status='Ongoing Events').count()
    events_conducted = event_status.count()
    upcoming_events = event_status.filter(status='Upcoming Events').count()

    context = {'events': event, 'ongoing_events': ongoing_events,
               'events_conducted': events_conducted, 'upcoming_events': upcoming_events}

    return render(request, 'events/dashboard.html', context)


def events(request):
    event = Event.objects.all()
    return render(request, 'events/events.html', {'events': event})


def tba(request):
    return HttpResponse('Customers')
# tba is given so that in future to change its name
