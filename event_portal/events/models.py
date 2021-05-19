from django.db import models

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200)
    limit = models.IntegerField()

    def __str__(self):
        return self.name
