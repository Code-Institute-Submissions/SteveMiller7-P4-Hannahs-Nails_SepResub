# Generated by Django 3.2.13 on 2022-06-07 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0025_auto_20220607_1413'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Appointment',
            new_name='Appointments',
        ),
    ]
