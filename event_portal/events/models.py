from django.db import models

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200)
    limit = models.IntegerField()

    def __str__(self):
        return self.name


class EventStatus(models.Model):
    STATUS = (
        ('Ongoing Events', 'Ongoing Events'),
        ('Events Conducted', 'Events Conducted'),
        ('Upcoming Events', 'Upcoming Events')
    )
    # ongoing_events = models.CharField(max_length=200)
    # events_conducted = models.CharField(max_length=200, null=True)
    # upcoming_events = models.CharField(max_length=200)
    events_created = models.ForeignKey(
        Event, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.status
