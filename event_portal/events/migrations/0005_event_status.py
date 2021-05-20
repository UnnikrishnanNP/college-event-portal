# Generated by Django 3.2.3 on 2021-05-20 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_eventstatus_events_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('Ongoing Events', 'Ongoing Events'), ('Events Conducted', 'Events Conducted'), ('Upcoming Events', 'Upcoming Events')], max_length=200, null=True),
        ),
    ]
