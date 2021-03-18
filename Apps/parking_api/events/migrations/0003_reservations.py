from django.db import migrations
import datetime

def populate_db(apps, schema_editor):
    Event = apps.get_model('events', 'Event')
    Lot = apps.get_model('events', 'Lot')
    Spot = apps.get_model('events', 'Spot')
    Customer = apps.get_model('events', 'Customer')
    Reservation = apps.get_model('events', 'Reservation')

    c1 = Customer(firstName='Jeremy',
                  lastName='Young',
                  email='yaj@gmail.com',
                  password='password',
                  credits='100'
    )
    c1.save()

    c2 = Customer(firstName='Logan',
                  lastName='Smith',
                  email='ls@gmail.com',
                  password='password',
                  credits='100'
    )
    c2.save()

    # Grab Events
    e1 = Event.objects.get(pk=1)
    e2 = Event.objects.get(pk=2)
    # Lots
    l1 = Lot.objects.get(pk=1)
    l2 = Lot.objects.get(pk=2)
    # one spot from each
    s1 = l1.spot_set.all()[0]
    s2 = l2.spot_set.all()[0]

    # create reservations
    r1 = Reservation(customer=c1,
                     spot=s1,
                     date=e1.startTime,
                     event=e1
    )
    r1.save()
    s1.reserved = True
    s1.save()

    r2 = Reservation(customer=c2,
                     spot=s2,
                     date=e2.startTime,
                     event=e2
    )
    r2.save()

    s2.reserved = True
    s2.save()

class Migration(migrations.Migration):
    dependencies = [
        ('events', '0001_initial'),
        ('events', '0002_events'),
    ]
    operations = [
        migrations.RunPython(populate_db),
    ]
