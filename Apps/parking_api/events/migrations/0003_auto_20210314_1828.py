# Generated by Django 3.1.7 on 2021-03-15 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_events'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spot',
            name='reservation',
        ),
        migrations.RemoveField(
            model_name='spot',
            name='reserved',
        ),
    ]
