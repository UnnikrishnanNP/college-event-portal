from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def home(request):
    return render(request, 'events/dashboard.html')


def events(request):
    event = Event.objects.all()
    return render(request, 'events/events.html', {'events': events})


def tba(request):
    return HttpResponse('Customers')
# tba is given so that in future to change its name
