from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'events/dashboard.html')


def events(request):
    return render(request, 'events/events.html')


def tba(request):
    return HttpResponse('Customers')
# tba is given so that in future to change its name
