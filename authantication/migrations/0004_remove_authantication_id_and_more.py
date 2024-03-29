# Generated by Django 5.0.2 on 2024-02-20 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authantication', '0003_remove_authantication_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authantication',
            name='id',
        ),
        migrations.RemoveField(
            model_name='authantication',
            name='password',
        ),
        migrations.RemoveField(
            model_name='authantication',
            name='user_name',
        ),
        migrations.AddField(
            model_name='authantication',
            name='police_station_location',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AddField(
            model_name='authantication',
            name='police_station_name',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AddField(
            model_name='authantication',
            name='state_speacial_code',
            field=models.IntegerField(default=False, primary_key=True, serialize=False),
        ),
    ]
