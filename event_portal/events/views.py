from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.


def home(request):
    event = Event.objects.all()
    # ongoing_events = event.filter(status='Ongoing Events').count()
    # events_conducted = event.filter(status='Events Conducted').count()
    # upcoming_events = event.filter(status='Upcoming Events').count()

    event_status = EventStatus.objects.all()
    ongoing_events = event_status.filter(status='Ongoing Events').count()
    events_completed = event_status.filter(status="Events Completed").count()
    upcoming_events = event_status.filter(status='Upcoming Events').count()

    context = {'events': event, 'ongoing_events': ongoing_events,
               'events_completed': events_completed, 'upcoming_events': upcoming_events}

    return render(request, 'events/dashboard.html', context)


def events(request):
    event = Event.objects.all()
    return render(request, 'events/events.html', {'events': event})


def new_event(request):
    form = NewEventForm()
    if request.method == 'POST':
        data = request.POST
        print('Printing POST : ', request.POST)
        form = NewEventForm(redirect)
        context = {'form': data}
        if form.is_valid():
            form.save()
            return redirect('/')

    elif request.method == 'GET':
        data = request.GET
        print('Printing GET : ', request.GET)
        form = NewEventForm(request)
        context = {'form': data}
        if form.is_valid():
            form.save()
            return render(request, 'events/new_event.html', context)

    else:
        context = {'form': form}
        return render(request, 'events/new_event.html', context)
# tba is given so that in future to change its name
