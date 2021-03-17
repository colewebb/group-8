from django.db import migrations
import datetime

# This is where the test populations for the database are defined

def populate_db(apps, schema_editor):
    # Lot owner
    LotOwner = apps.get_model('events', 'LotOwner')

    lo1 = LotOwner(firstName='Supreme',
                   lastName='Owner',
                   email='supreme.owner@gmail.com',
                   password='password',
                   credits=2000
    )

    # example events
    Event = apps.get_model('events', 'Event')

    e1 = Event(name='USU v BYU',
               startTime = datetime.datetime.now(), # lazy
               endTime = datetime.datetime.now(), # again, lazy
               address = '900 E 900 N, Logan, UT 84322')
    e1.save()

    e2 = Event(name='USU Wind Symphony Concert',
               startTime = datetime.datetime.now(),
               endTime = datetime.datetime.now(),
               address = '600 E 1150 N, North Logan, UT 84341')
    e2.save()

    # sample lots
    Lot = apps.get_model('events', 'Lot')

    l1 = Lot(owner=lo1,
            name='East Stadium',
            address='900 E 1000 N Logan UT, 84341',
            openTime=datetime.datetime.now(),
            closeTime=datetime.datetime.now(),
            capacityActual=500,
            capacityMax=500)
    l1.save()
    l1.events.add(e1,e2)

    l2 = Lot(owner=lo1,
            name='Blue Terrace',
            address='850 E Aggie BLVD Logan, UT 84321',
            openTime=datetime.datetime.now(),
            closeTime=datetime.datetime.now(),
            capacityActual=300,
            capacityMax=300)
    l2.save()
    l2.events.add(e2)


    # give each lot 5 of each spot Type (small, medium, large)
    Spot = apps.get_model('events', 'Spot')

    for i in range(5):
        small1 = Spot(l1,
                      size='small',
                      cost=10,
                      )
        small1.save()
        small2 = Spot(l2,
                      size='small',
                      cost=10,
                      )
        small2.save()
    for i in range(5):
        medium1 = Spot(l1,
                      size='medium',
                      cost=10,
                      )
        medium1.save()
        medium2 = Spot(l2,
                      size='medium',
                      cost=10,
                      )
        medium2.save()
    for i in range(5):
        large1 = Spot(l1,
                      size='large',
                      cost=10,
                      )
        large1.save()
        large2 = Spot(l2,
                      size='large',
                      cost=10,
                      )
        large2.save()


class Migration(migrations.Migration):
    dependencies = [
        ('events', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(populate_db),
    ]
