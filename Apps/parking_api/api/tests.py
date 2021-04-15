from django.test import TestCase
from api.models import ParentLot, Lot, Reservation, Event
from django.contrib.auth.models import User
import datetime
import unittest
import os

class TestDatabase(TestCase):
    def testParentLot(self):
        user1 = User.objects.create_user(
            username='test', 
            email='test@gmail.com', 
            password='password',
            last_login=datetime.datetime.now()
        )
        user1.save()
        pl = ParentLot(
            owner=user1,
            name="Test Lot",
            created=datetime.datetime.now(),
            address="Somewhere, anywhere",
            capSmallMax=0,
            capMediumMax=10,
            capLargeMax=20
        )
        pl.save()
        self.assertEqual(pl.name, "Test Lot")
        self.assertEqual(pl.address, "Somewhere, anywhere")
        self.assertEqual(pl.capSmallMax, 0)
        self.assertEqual(pl.capMediumMax, 10)
        self.assertEqual(pl.capLargeMax, 20)

    def testUser(self):
        user1 = User.objects.create_user(
            username='test', 
            email='test@gmail.com', 
            password='password',
            last_login=datetime.datetime.now()
        )
        user1.save()
        self.assertEqual(user1.username, "test")
        self.assertEqual(user1.email, "test@gmail.com")
        

    def testLot(self):
        user1 = User.objects.create_user(
            username='test', 
            email='test@gmail.com', 
            password='password',
            last_login=datetime.datetime.now()
        )
        user1.save()
        pl = ParentLot(
            owner=user1,
            name="Test Lot",
            created=datetime.datetime.now(),
            address="Somewhere, anywhere",
            capSmallMax=0,
            capMediumMax=10,
            capLargeMax=20
        )
        pl.save()
        e2 = Event(name='USU Wind Symphony', created=datetime.datetime.now(),
               startTime=datetime.datetime(2021, 5, 20, 18),
               endTime=datetime.datetime(2021, 5, 20, 20),
               address='600 E 1150 N, North Logan, UT 84341'
               )
        e2.save()
        l = Lot(
            created=datetime.datetime.now(),
            owner=user1,
            capSmallMax=10,
            capMediumMax=20,
            capLargeMax=5,
            openTime=datetime.time(17, 0, 0),
            closeTime=datetime.time(23, 0, 0),
            capSmallActual=7,
            capMediumActual=15,
            capLargeActual=4,
            costSmall=10.00,
            costMedium=15.00,
            costLarge=20.00,
            event=e2,
            parentLot=pl
        )
        l.save()
        self.assertEqual(l.owner, user1)
        self.assertEqual(l.capSmallMax, 10)
        self.assertEqual(l.capMediumMax, 20)
        self.assertEqual(l.capLargeMax, 5)
        self.assertEqual(l.openTime, datetime.time(17, 0, 0))
        self.assertEqual(l.closeTime, datetime.time(23, 0, 0))
        self.assertEqual(l.capSmallActual, 7)
        self.assertEqual(l.capMediumActual, 15)
        self.assertEqual(l.capLargeActual, 4)
        self.assertEqual(l.costSmall, 10.00)
        self.assertEqual(l.costMedium, 15.00)
        self.assertEqual(l.costLarge, 20.00)
        self.assertEqual(l.event, e2)
        self.assertEqual(l.parentLot, pl)

    def testEvent(self):
        e1 = Event(
            name='test', 
            created=datetime.datetime.now(),
            startTime=datetime.datetime(2021, 5, 17, 19),
            endTime=datetime.datetime(2021, 5, 17, 22),
            address="somewhere, but not here"
        )
        e1.save()
        self.assertEqual(e1.name, "test")
        self.assertEqual(e1.startTime, datetime.datetime(2021, 5, 17, 19))
        self.assertEqual(e1.endTime, datetime.datetime(2021, 5, 17, 22))
        self.assertEqual(e1.address, "somewhere, but not here")

    def testReservation(self):
        user1 = User.objects.create_user(
            username='test', 
            email='test@gmail.com', 
            password='password',
            last_login=datetime.datetime.now()
        )
        pl = ParentLot(
            owner=user1,
            name="Test Lot",
            created=datetime.datetime.now(),
            address="Somewhere, anywhere",
            capSmallMax=0,
            capMediumMax=10,
            capLargeMax=20
        )
        pl.save()
        e1 = Event(
            name='test', 
            created=datetime.datetime.now(),
            startTime=datetime.datetime(2021, 5, 17, 19),
            endTime=datetime.datetime(2021, 5, 17, 22),
            address="somewhere, but not here"
        )
        e1.save()
        l = Lot(
            created=datetime.datetime.now(),
            owner=user1,
            capSmallMax=10,
            capMediumMax=20,
            capLargeMax=5,
            openTime=datetime.time(17, 0, 0),
            closeTime=datetime.time(23, 0, 0),
            capSmallActual=7,
            capMediumActual=15,
            capLargeActual=4,
            costSmall=10.00,
            costMedium=15.00,
            costLarge=20.00,
            event=e1,
            parentLot=pl
        )
        l.save()
        r = Reservation(
            owner=user1,
            lot=l,
            size='small',
            date=l.event.startTime,
            event=l.event
        )
        r.save()
        self.assertEqual(r.owner, user1)
        self.assertEqual(r.lot, l)
        self.assertEqual(r.size, 'small')
        self.assertEqual(r.date, l.event.startTime)
        self.assertEqual(r.event, l.event)
