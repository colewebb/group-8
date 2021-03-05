from django.contrib import admin

from .models import User, Customer, Attendant
from .models import LotOwner, Administrator, Reservation
from .models import Lot, Spot, Event, Root

# Register your models here.

admin.site.register(Customer)
admin.site.register(Attendant)
admin.site.register(LotOwner)
admin.site.register(Administrator)
admin.site.register(Reservation)
admin.site.register(Lot)
admin.site.register(Spot)
admin.site.register(Event)
admin.site.register(Root)
