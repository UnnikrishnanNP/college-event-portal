from django.db import models

# Create your models here.


class Event(models.Model):
    STATUS = (
        ('Ongoing Events', 'Ongoing Events'),
        ('Events Conducted', 'Events Conducted'),
        ('Upcoming Events', 'Upcoming Events')
    )
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200)
    limit = models.IntegerField()
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.name


class EventStatus(models.Model):
    STATUS = (
        ('Ongoing Events', 'Ongoing Events'),
        ('Events Completed', 'Events Completed'),
        ('Upcoming Events', 'Upcoming Events'),
    )
    events_created = models.ForeignKey(
        Event, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.status


class NewEvent(models.Model):
    title = models.CharField(max_length=200, null=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=200, null=True)
    limit = models.IntegerField()
    description = models.CharField(max_length=200, null=True)
    banner = models.CharField(max_length=200)
