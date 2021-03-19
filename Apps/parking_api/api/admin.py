from django.contrib import admin

from .models import Lot, Spot, Event, Reservation

# Register your models here.

admin.site.register(Reservation)
admin.site.register(Lot)
admin.site.register(Spot)
admin.site.register(Event)
