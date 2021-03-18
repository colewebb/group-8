# Generated by Django 3.1.7 on 2021-03-17 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('credits', models.DecimalField(decimal_places=2, max_digits=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('credits', models.DecimalField(decimal_places=2, max_digits=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('address', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('openTime', models.DateTimeField()),
                ('closeTime', models.DateTimeField()),
                ('capacityActual', models.IntegerField()),
                ('capacityMax', models.IntegerField()),
                ('events', models.ManyToManyField(to='events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='LotOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('credits', models.DecimalField(decimal_places=2, max_digits=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Root',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=30)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=100)),
                ('reserved', models.BooleanField(default=False)),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.lot')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.customer')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('spot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.spot')),
            ],
        ),
        migrations.AddField(
            model_name='lot',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.lotowner'),
        ),
        migrations.CreateModel(
            name='Attendant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.lot')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
