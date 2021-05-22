from django.forms import ModelForm
from .models import Event


class NewEventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
