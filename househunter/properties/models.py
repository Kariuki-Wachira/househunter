from django.db import models
from django.db.models.fields import TextField
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

class Property(models.Model):
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    availabilitystatus = models.TextField(default= 'n/a')
    price = models.TextField(default= 'n/a')
    contacts = models.TextField(default= 'n/a')
    description = models.TextField()


    def __str__(self):
        return self.description

   