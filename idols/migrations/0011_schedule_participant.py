# Generated by Django 4.1.7 on 2023-03-06 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idols', '0010_alter_schedule_scheduletitle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='participant',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]