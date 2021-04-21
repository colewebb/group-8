from django.db import models

# Create your models here.

SPOT_SIZES = [('small', 'small'), ('medium', 'medium'), ('large', 'large')]


class Event(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ", " + self.address + " (" + str(self.startTime) + ")"

class ParentLot(models.Model):
    owner = models.ForeignKey('auth.User', related_name='parent_lots', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    # costSmall = models.DecimalField(max_digits=100, decimal_places=2)
    capSmallMax = models.IntegerField()
    # costMedium = models.DecimalField(max_digits=100, decimal_places=2)
    capMediumMax = models.IntegerField()
    # costLarge = models.DecimalField(max_digits=100, decimal_places=2)
    capLargeMax = models.IntegerField()

    def __str__(self):
        return "Parent: " + self.name + ", " + self.address + " (" + self.owner.username + ")"


class Lot(models.Model):
    # capacities for each spot type
    # open time for the lot for the specific event (can be default 30 min before event)
    # points to a 'concrete' lot and an event
    owner = models.ForeignKey('auth.User', related_name='lots', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    openTime = models.TimeField()
    closeTime = models.TimeField()
    costSmall = models.DecimalField(max_digits=100, decimal_places=2)
    capSmallActual = models.IntegerField()
    capSmallMax = models.IntegerField()
    costMedium = models.DecimalField(max_digits=100, decimal_places=2)
    capMediumActual = models.IntegerField()
    capMediumMax = models.IntegerField()
    costLarge = models.DecimalField(max_digits=100, decimal_places=2)
    capLargeActual = models.IntegerField()
    capLargeMax = models.IntegerField()
    event = models.ForeignKey(Event, related_name='lots', on_delete=models.CASCADE)
    parentLot = models.ForeignKey(ParentLot, related_name='assignments', on_delete=models.CASCADE)

    def __str__(self):
        return self.parentLot.name + ", " + self.parentLot.address + " (" + self.owner.username + ")"

class Reservation(models.Model):
    owner = models.ForeignKey('auth.User', related_name='reservations', on_delete=models.CASCADE)
    lot = models.ForeignKey(Lot, related_name='reservation', on_delete=models.CASCADE)
    size = models.CharField(choices=SPOT_SIZES, max_length=30)
    date = models.DateTimeField()
    event = models.ForeignKey(Event, related_name='reservations', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner.username + "\n" + str(self.event) + "\n" + "(" + str(self.lot) + ")"

class Balance(models.Model):
    owner = models.OneToOneField('auth.User', related_name='balance', on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=100, decimal_places=2)
