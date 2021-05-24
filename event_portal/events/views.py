from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Event
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import NewEventForm, UpdateEventForm, CreateUserForm, RegisterEventForm
from django.contrib.auth.forms import UserCreationForm
from .decoraters import unauthenticated_user, allowed_users, admin_only
# Create your views here.


# register page view
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='users')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'events/register.html', context)


# login page view
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'events/login.html', context)

# logout page view


def logoutUser(request):
    logout(request)
    return redirect('login')


# home page view
@login_required(login_url='login')
@admin_only
def home(request):
    event = Event.objects.all()
    ongoing_events = event.filter(status='Ongoing Events').count()
    events_completed = event.filter(status='Events Completed').count()
    upcoming_events = event.filter(status='Upcoming Events').count()

    context = {'events': event, 'ongoing_events': ongoing_events,
               'events_completed': events_completed, 'upcoming_events': upcoming_events}

    return render(request, 'events/dashboard.html', context)

# user profile page view


@login_required(login_url='login')
@allowed_users(allowed_roles=['users'])
def userProfile(request):
    event = Event.objects.filter(register=True)
    ongoing_events = event.filter(status='Ongoing Events').count()
    events_completed = event.filter(status='Events Completed').count()
    upcoming_events = event.filter(status='Upcoming Events').count()
    context = {'event': event, 'ongoing_events': ongoing_events,
               'events_completed': events_completed, 'upcoming_events': upcoming_events}
    return render(request, 'events/user-profile.html', context)

# events page view


@login_required(login_url='login')
def events(request):
    event = Event.objects.all()
    return render(request, 'events/events.html', {'events': event})


# new event page view
@login_required(login_url='login')
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

# Register event view page


@login_required(login_url='login')
# @allowed_users(allowed_roles=['users', 'admins'])
def registerEvent(request, pk):
    event = Event.objects.all()

    register_event = Event.objects.get(id=pk)
    form = RegisterEventForm(instance=register_event)
    if request.method == "POST":
        form = RegisterEventForm(request.POST, instance=register_event)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form, 'event': event}
    return render(request, 'events/register-event.html', context)

# update event view


@login_required(login_url='login')
def updateEvent(request, pk):

    update_event = Event.objects.get(id=pk)
    form = UpdateEventForm(instance=update_event)
    if request.method == "POST":
        form = UpdateEventForm(request.POST, instance=update_event)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'events/update_event.html', context)


# delete event view
@login_required(login_url='login')
def deleteEvent(request, pk):
    event_link = Event.objects.get(id=pk)
    if request.method == 'POST':
        event_link.delete()
        return redirect('/')
    context = {'name': event_link}
    return render(request, 'events/delete.html', context)
