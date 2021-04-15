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

    # def testLot(self):
    #     l = Lot(
    #         created=datetime.now(),
    #         capSmallMax=10,
    #         capMediumMax=20,
    #         capLargeMax=5,
    #         
    #     )
