from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=30) # probably change this later to something more secure
    role = models.CharField(max_length=30)

    credits = models.DecimalField(max_digits=100, decimal_places=2)

    # def __str__(self):
    #     return "(" + self.lastName + ", " + self.firstName + ") " + self.email

class Event(models.Model):
    name = models.CharField(max_length=30)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    address = models.CharField(max_length=30)

    # def createEvent():
    #     pass
    #
    # def notifyLotOwners():
    #     pass

class Lot(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    openTime = models.DateTimeField()
    closeTime = models.DateTimeField()
    capacityActual = models.IntegerField()
    capacityMax = models.IntegerField()
    events = models.ManyToManyField(Event)

    # def addReservation(reservation):
    #     pass

class Attendant(User):
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)

    # def verify(reservation):
    #     pass

class Spot(models.Model):
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    size = models.CharField(max_length=30)
    cost = models.DecimalField(max_digits=100, decimal_places=2)
    reserved = models.BooleanField(default=False)

class Reservation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
    date = models.DateTimeField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    # def confirmReservation():
    #     pass
    #
    # def cancelReservation():
    #     pass
    #
    # def getQRCode():
    #     pass


class Root(models.Model):
    events = [] # list of events
    admins = [] # list of administrators
