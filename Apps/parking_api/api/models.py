from django.db import models

# Create your models here.

SPOT_SIZES = [(0, 'small'), (1, 'medium'), (2, 'large')]


class Event(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ", " + self.address + " (" + str(self.startTime) + ")"


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

    def __str__(self):
        return self.name + ", " + self.address + " (" + self.owner.username + ")"


class Spot(models.Model):
    lot = models.ForeignKey(Lot, related_name='spots', on_delete=models.CASCADE)
    size = models.CharField(choices=SPOT_SIZES, max_length=30)
    cost = models.DecimalField(max_digits=100, decimal_places=2)
    reserved = models.BooleanField(default=False)

    def __str__(self):
        return SPOT_SIZES[int(self.size)][1] + " " + str(self.id) + " (" + self.lot.name + ")"


class Reservation(models.Model):
    owner = models.ForeignKey('auth.User', related_name='reservations', on_delete=models.CASCADE)
    spot = models.ForeignKey(Spot, related_name='reservation', on_delete=models.CASCADE)
    date = models.DateTimeField()
    event = models.ForeignKey(Event, related_name='event', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner.username + " (" + str(self.event) + ")"


# class Root(models.Model):
#     events = [] # list of events
#     admins = [] # list of administrators
