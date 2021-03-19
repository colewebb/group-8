from django.db import models

# Create your models here.

SPOT_SIZES = [(0, 'small'), (1, 'medium'), (2, 'large')]


class Event(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    address = models.CharField(max_length=100)


class Lot(models.Model):
    owner = models.ForeignKey('auth.User', related_name='lots', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    openTime = models.DateTimeField()
    closeTime = models.DateTimeField()
    capacityActual = models.IntegerField()
    capacityMax = models.IntegerField()
    events = models.ManyToManyField(Event)


class Spot(models.Model):
    lot = models.ForeignKey(Lot, related_name='spots', on_delete=models.CASCADE)
    size = models.CharField(choices=SPOT_SIZES, max_length=30)
    cost = models.DecimalField(max_digits=100, decimal_places=2)
    reserved = models.BooleanField(default=False)


class Reservation(models.Model):
    owner = models.ForeignKey('auth.User', related_name='reservations', on_delete=models.CASCADE)
    spot = models.ForeignKey(Spot, related_name='reservation', on_delete=models.CASCADE)
    date = models.DateTimeField()
    event = models.ForeignKey(Event, related_name='event', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


# class Root(models.Model):
#     events = [] # list of events
#     admins = [] # list of administrators