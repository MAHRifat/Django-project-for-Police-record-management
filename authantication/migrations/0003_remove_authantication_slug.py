# Generated by Django 5.0.2 on 2024-02-20 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authantication', '0002_authantication_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authantication',
            name='slug',
        ),
    ]
