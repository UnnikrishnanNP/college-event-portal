from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Event


class NewEventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
            'event_name', 'location', 'limit', 'status'
        ]


class UpdateEventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
            'event_name',
            'location',
            'limit'
        ]


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2'
        ]


class RegisterEventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
            'full_name',
            'email',
            'phone_number',
            'event_name',
            'location',
            'limit',
            'register'
        ]


class UnregisterEventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
            'full_name',
            'email',
            'phone_number',
            'event_name',
            'location',
            'limit',
            'register'
        ]
