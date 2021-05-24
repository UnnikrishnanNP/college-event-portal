from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Event(models.Model):
    STATUS = (
        ('Ongoing Events', 'Ongoing Events'),
        ('Events Completed', 'Events Completed'),
        ('Upcoming Events', 'Upcoming Events')
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200)
    limit = models.IntegerField()
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    register = models.BooleanField(null=True)
    full_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=250, null=True)
    phone_number = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.event_name
