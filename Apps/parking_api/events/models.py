from django.db import models

# Create your models here.

# Many methods have yet to be implemented.

class User(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=30) # probably change this later to something more secure

    def __str__(self):
        return "(" + lastName + ", " + firstName + ") " + EmailField

    # this is necessary for abstract inheritance in Django
    class Meta:
        abstract = True

class Customer(User):
    credits = models.DecimalField(max_digits=100, decimal_places=2)
    reservations = [] # list of reservations

    def addReservation(reservation):
        reservations.append(reservation)

    def addCredits(x):
        credits += x

class Attendant(User):
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)

    def verify(reservation):
        pass

class LotOwner(User):
    credits = models.DecimalField(max_digits=100, decimal_places=2)
    lots = [] # list of lots

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
    id = models.IntegerField()

    def confirmReservation():
        pass

    def cancelReservation():
        pass

    def getQRCode():
        pass
