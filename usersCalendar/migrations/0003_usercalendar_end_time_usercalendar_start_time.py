# Generated by Django 4.1.7 on 2023-03-06 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersCalendar', '0002_alter_usercalendar_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercalendar',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usercalendar',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
