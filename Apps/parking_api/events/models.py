from django.db import models

# Create your models here.

# Many methods have yet to be implemented.

class User(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=30) # probably change this later to something more secure

    def __str__(self):
        return "(" + self.lastName + ", " + self.firstName + ") " + self.email

    # this is necessary for abstract inheritance in Django
    class Meta:
        abstract = True

class Customer(User):
    credits = models.DecimalField(max_digits=100, decimal_places=2)
    # Customer may have many reservations, but this is defined
    # in the Reservation class

    def addCredits(x):
        credits += x

class Lot(models.Model):
    name = models.CharField(max_length=30)
    # distance
    address = models.CharField(max_length=30)
    spots = [] # list of Spots
    openTime = models.DateTimeField()
    closeTime = models.DateTimeField()
    capacityActual = models.IntegerField()
    capacityMax = models.IntegerField()
    reservations = [] # list of reservations
    attendants = [] # list of attendants

    def addReservation(reservation):
        pass

class Attendant(User):
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)

    def verify(reservation):
        pass

class LotOwner(User):
    credits = models.DecimalField(max_digits=100, decimal_places=2)
    lots = [] # list of Lots

    def addLotToEvent(lot, event):
        pass

    def addNewLot(lot):
        pass

class Administrator(User):
    credits = models.DecimalField(max_digits=100, decimal_places=2)

class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    spotType = models.CharField(max_length=30)
    date = models.DateTimeField()
    address = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    reservation_id = models.IntegerField()

    def confirmReservation():
        pass

    def cancelReservation():
        pass

    def getQRCode():
        pass


class Spot(models.Model):
    size = models.CharField(max_length=30)
    cost = models.DecimalField(max_digits=100, decimal_places=2)
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    reserved = models.BooleanField(default=False)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)

class Event(models.Model):
    name = models.CharField(max_length=30)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    address = models.CharField(max_length=30)
    # Event has a one-to-many relationship with lots, but this
    # is defined in the Lot class, not in the Event class

    def createEvent():
        pass

    def notifyLotOwners():
        pass

class Root(models.Model):
    events = [] # list of events
    admins = [] # list of administrators
