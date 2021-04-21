from django.db import migrations
import datetime

def populate_db(apps, schema_editor):
    # set up some users
    from django.contrib.auth.models import User
    user1 = User.objects.create_user(username='austin', email='asmith@gmail.com', password='password',
                 last_login=datetime.datetime.now())
    user1.save()
    user2 = User.objects.create_user(username='cole', email='cwebb@gmail.com', password='password',
                 last_login=datetime.datetime.now())
    user2.save()
    user3 = User.objects.create_user(username='logan', email='lsmith@gmail.com', password='password',
                 last_login=datetime.datetime.now())
    user3.save()
    user4 = User.objects.create_user(username='LotOwner', email='iownlots@gmail.com', password='password',
                last_login=datetime.datetime.now())
    user4.save()
    superuser = User.objects.create_superuser(username="admin", email="admin@fake.com", password="admin", last_login=datetime.datetime.now())
    superuser.save()

    # Now performed automatically by signals
    
    # from api.models import Balance
    # b1 = Balance(owner=user1, value=50)
    # b1.save()
    # b2 = Balance(owner=user2, value=50)
    # b2.save()
    # b3 = Balance(owner=user3, value=50)
    # b3.save()
    # b4 = Balance(owner=user4, value=50)
    # b4.save()
    # b5 = Balance(owner=superuser, value=250)
    # b5.save()

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

    superuser = User.objects.create_superuser(username='jeremy',
            email='young.a.jeremy@gmail.com',
            password='password',
            last_login=datetime.datetime.now())
    superuser.save()

    # set up some lots
    from api.models import ParentLot
    p1 = ParentLot(owner=superuser,
             name='Maverik Stadium',
             address='875 Douglas Dr, Logan, UT 84321',
             created=datetime.datetime.now(),
             capSmallMax=80,
             capMediumMax=40,
             capLargeMax=10
    )
    p1.save()

    p2 = ParentLot(owner=user4,
             name='Gr8 Parking',
             address='Engineering Lab Walkway, Logan, UT 84321',
             created=datetime.datetime.now(),
             capSmallMax=30,
             capMediumMax=5,
             capLargeMax=0
    )
    p2.save()


    # assign some lots to events
    from api.models import Lot
    l1 = Lot(
        owner=superuser,
        openTime=datetime.time(17, 0, 0),
        closeTime=datetime.time(23, 0, 0),
        costSmall=10.00,
        capSmallActual=50,
        capSmallMax=50,
        costMedium=15.00,
        capMediumActual=20,
        capMediumMax=20,
        costLarge=20.00,
        capLargeActual=10,
        capLargeMax=10,
        event=e1,
        parentLot=p1
    )
    l1.save()

    l2 = Lot(
        owner=user4,
        openTime=datetime.time(14, 0, 0),
        closeTime=datetime.time(22, 0, 0),
        costSmall=10.00,
        capSmallActual=50,
        capSmallMax=50,
        costMedium=15.00,
        capMediumActual=20,
        capMediumMax=20,
        costLarge=0,
        capLargeActual=0,
        capLargeMax=0,
        event=e2,
        parentLot=p2
    )
    l2.save()

    # a couple reservations
    from api.models import Reservation
    r1 = Reservation(
        owner=user1,
        lot=l2,
        size='small',
        date=l2.event.startTime,
        event=l2.event
    )
    r1.save()

    # this step is only necessary in the migrations, performed automatically
    # upon api call
    l2.capSmallActual -= 1
    l2.save()

    r2 = Reservation(
        owner=user3,
        lot=l1,
        size='medium',
        date=l1.event.startTime,
        event=l1.event
    )
    r2.save()

    # this step is only necessary in the migrations, performed automatically
    # upon api call
    l1.capMediumActual -= 1
    l1.save()

    # create some groups
    from django.contrib.auth.models import Group
    owners = Group(id=1, name="Owners")
    owners.save()
    user4.groups.add(owners)

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_db),
    ]
