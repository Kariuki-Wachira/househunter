from django.contrib import admin

# Register your models here.

from . models import Property, Location, Staffrequest, Wishlist

admin.site.site_header= 'HOUSE MANAGEMENT ADMIN'
admin.site.register(Staffrequest)
admin.site.register(Property)
admin.site.register(Location)
admin.site.register(Wishlist)



