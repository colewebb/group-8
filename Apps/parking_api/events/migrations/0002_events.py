from django.db import migrations
import datetime

# This is where the test populations for the database are defined

def populate_db(apps, schema_editor): 
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

    l1 = Lot(name='East Stadium',
            address='900 E 1000 N Logan UT, 84341',
            openTime=datetime.datetime.now(),
            closeTime=datetime.datetime.now(),
            capacityActual=500,
            capacityMax=500)
    l1.save()
    l1.events.add(e1,e2)

    l2 = Lot(name='Blue Terrace',
            address='850 E Aggie BLVD Logan, UT 84321',
            openTime=datetime.datetime.now(),
            closeTime=datetime.datetime.now(),
            capacityActual=300,
            capacityMax=300)
    l2.save()


    #sample spots
    Spot = apps.get_model('events', 'Spot')

    s1 = Spot(lot=l1, size='small', cost=7.50)
    s1.save()


class Migration(migrations.Migration):
    dependencies = [
        ('events', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(populate_db),
    ]
