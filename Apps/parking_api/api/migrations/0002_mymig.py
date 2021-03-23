from django.db import migrations
import datetime

def populate_db(apps, schema_editor):
    # set up some users
    from django.contrib.auth.models import User
    user1 = User(username='austin', email='asmith@gmail.com', password='password')
    user1.save()
    user2 = User(username='cole', email='cwebb@gmail.com', password='password')
    user2.save()
    user3 = User(username='logan', email='lsmith@gmail.com', password='password')
    user3.save()

    # set up some events
    from api.models import Event
    e1 = Event(name='USU v. BYU', created=datetime.datetime.now(),
               startTime=datetime.datetime(2021, 5, 17, 19),
               endTime=datetime.datetime(2021, 5, 17, 22),
               address='900 E 900 N, Logan, UT 84322'
               )
    e1.save()

    e2 = Event(name='USU Wind Symphony', created=datetime.datetime.now(),
               startTime=datetime.datetime(2021, 5, 20, 18),
               endTime=datetime.datetime(2021, 5, 20, 20),
               address='600 E 1150 N, North Logan, UT 84341'
               )
    e2.save()

    superuser = User.objects.get(username='jeremy')
    # set up some lots (only createable by superusers)
    from api.models import Lot
    l1 = Lot(owner=superuser,
             name='Maverik Stadium',
             address='875 Douglas Dr, Logan, UT 84321',
             created=datetime.datetime.now(),
             openTime=datetime.time(8, 0, 0),
             closeTime=datetime.time(23, 0, 0),
             costSmall=10.00,
             capSmallActual=80,
             capSmallMax=80,
             costMedium=15.00,
             capMediumActual=40,
             capMediumMax=40,
             costLarge=20.00,
             capLargeActual=10,
             capLargeMax=10
    )
    l1.events.add(e1)
    l1.save()

    l2 = Lot(owner=superuser,
             name='Gr8 Parking',
             address='Engineering Lab Walkway, Logan, UT 84321',
             created=datetime.datetime.now(),
             openTime=datetime.time(8, 0, 0),
             closeTime=datetime.time(23, 0, 0),
             costSmall=10.00,
             capSmallActual=30,
             capSmallMax=30,
             costMedium=15.00,
             capMediumActual=5,
             capMediumMax=5,
             costLarge=20.00,
             capLargeActual=0,
             capLargeMax=0
    )
    l2.events.add(e1, e2)
    l2.save()

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_db),
    ]
