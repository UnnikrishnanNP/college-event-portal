from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Event
from .forms import NewEventForm
# Create your views here.


def home(request):
    event = Event.objects.all()
    ongoing_events = event.filter(status='Ongoing Events').count()
    events_completed = event.filter(status='Events Completed').count()
    upcoming_events = event.filter(status='Upcoming Events').count()

    context = {'events': event, 'ongoing_events': ongoing_events,
               'events_completed': events_completed, 'upcoming_events': upcoming_events}

    return render(request, 'events/dashboard.html', context)


def events(request):
    event = Event.objects.all()
    return render(request, 'events/events.html', {'events': event})


def newEvent(request):

    form = NewEventForm()

    if request.method == "POST":
        print(request.POST)
        # print("Printing Form : ", request.POST)
        form = NewEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'events/new_event.html', context)


def updateEvent(request, pk):
    form = NewEventForm()
    context = {'form': form}
    return render(request, 'events/new_event.html', context)

    # def deleteEvent(request, pk):
    #     event_link = Event.objects.get(id=pk)
    #     context = {'event_link': event_link}
    #     return render(request, 'events/delete.html', context)
