# Generated by Django 3.1.7 on 2021-04-07 19:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_mymig'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'permissions': [('create', 'can create an event'), ('update', 'can modify an event'), ('delete', 'can delete an event')]},
        ),
        migrations.AlterModelOptions(
            name='lot',
            options={'permissions': {('create', 'can create a lot assignment'), ('update', 'can modify a lot assignment'), ('delete', 'can delete a lot assignment')}},
        ),
        migrations.AlterModelOptions(
            name='parentlot',
            options={'permissions': {('create', 'can create a parent lot'), ('delete', 'can delete a parent lot'), ('update', 'can modify a parent lot')}},
        ),
        migrations.AlterModelOptions(
            name='reservation',
            options={'permissions': {('delete', 'can delete a reservation'), ('create', 'can create a reservation')}},
        ),
        migrations.CreateModel(
            name='LotOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
