# Generated by Django 5.0.2 on 2024-02-20 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime_record_check', '0003_rename_dob_number_record_entry_dob_birth_certification_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record_entry_dob',
            name='Birth_certification_number',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
