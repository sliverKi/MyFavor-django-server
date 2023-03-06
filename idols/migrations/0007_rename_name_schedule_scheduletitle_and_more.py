# Generated by Django 4.1.7 on 2023-03-06 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idols', '0006_remove_schedule_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='name',
            new_name='ScheduleTitle',
        ),
        migrations.AlterField(
            model_name='idol',
            name='idol_gender',
            field=models.CharField(choices=[('Women', 'Women'), ('Man', 'Man')], max_length=5),
        ),
        migrations.AlterField(
            model_name='idol',
            name='idol_group',
            field=models.CharField(blank=True, choices=[('GirlGroup', 'GirlGroup'), ('BoyGroup', 'BoyGroup')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='idol',
            name='idol_solo',
            field=models.CharField(blank=True, choices=[('GirlSolo', 'GirlSolo'), ('BoySolo', 'BoySolo')], max_length=30, null=True),
        ),
    ]
