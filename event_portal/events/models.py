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
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200)
    limit = models.IntegerField()
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.name
