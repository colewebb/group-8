from django.contrib import admin

from .models import Lot, ParentLot, Event, Reservation

# Register your models here.

admin.site.register(Reservation)
admin.site.register(Lot)
admin.site.register(ParentLot)
admin.site.register(Event)
