from django.db import migrations
import datetime

# This is where the test populations for the database are defined

def populate_db(apps, schema_editor):
    # example Customers
    Customer = apps.get_model('events', 'Customer')

    c1 = Customer(firstName='Jeremy', lastName='Young', email='young.a.jeremy@gmail.com',
                    password='password', credits=500)
    c1.save()

    c2 = Customer(firstName='Cole', lastName='Webb', email='email@gmail.com',
                    password='password', credits=500)
    c2.save()

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

class Migration(migrations.Migration):
    dependencies = [
        ('events', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(populate_db),
    ]
