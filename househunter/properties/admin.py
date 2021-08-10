from django.contrib import admin

# Register your models here.

from . models import Property, Location

admin.site.register(Property)
admin.site.register(Location)



