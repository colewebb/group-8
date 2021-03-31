from django.contrib import admin

from .models import Lot, AssignedLot, Event, Reservation

# Register your models here.

admin.site.register(Reservation)
admin.site.register(Lot)
admin.site.register(AssignedLot)
admin.site.register(Event)
