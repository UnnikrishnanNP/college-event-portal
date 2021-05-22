from django.forms import ModelForm
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
