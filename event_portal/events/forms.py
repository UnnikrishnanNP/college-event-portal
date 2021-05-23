from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Event


class NewEventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class UpdateEventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
            'name',
            'location',
            'limit'
        ]


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2'
        ]
