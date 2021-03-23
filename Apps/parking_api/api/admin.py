from django.contrib import admin

from .models import Lot, Event, Reservation

# Register your models here.

admin.site.register(Reservation)
admin.site.register(Lot)
admin.site.register(Event)
