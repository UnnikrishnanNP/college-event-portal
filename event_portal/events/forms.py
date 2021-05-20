from django.forms import ModelForm
from .models import *


class NewEventForm(ModelForm):
    class Meta:
        model = NewEvent
        fields = '__all__'
