from django.db import migrations

# This is where the test populations for the database are defined

def populate_db(apps, schema_editor):
    pass

class Migration(migrations.Migration):
    dependencies = [
        ('events', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(populate_db),
    ]
