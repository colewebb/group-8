from django.db import migrations
import datetime

def populate_db(apps, schema_editor):
    # example Customers
    Customer = apps.get_model('events', 'Customer')

    c1 = Customer(firstName='Jeremy', lastName='Young', email='young.a.jeremy@gmail.com',
                    password='password', credits=500)
    c1.save()

    c2 = Customer(firstName='Cole', lastName='Webb', email='email@gmail.com',
                    password='password', credits=500)
    c2.save()

    Reservation = apps.get_model('events', 'Reservation')

    r1 = Reservation(customer=c1,
                    spotType='small',
                    date=datetime.datetime.now(),
                    address='home',
                    price=20.00,
                    reservation_id=1)
    r1.save()

    r2 = Reservation(customer=c1,
                    spotType='medium',
                    date=datetime.datetime.now(),
                    address='school',
                    price=30.00,
                    reservation_id=2)
    r2.save()

class Migration(migrations.Migration):
    dependencies = [
        ('events', '0001_initial'),
        ('events', '0002_events'),
    ]
    operations = [
        migrations.RunPython(populate_db),
    ]
