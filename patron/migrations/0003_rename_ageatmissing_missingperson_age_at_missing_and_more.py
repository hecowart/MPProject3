# Generated by Django 4.2.2 on 2023-06-14 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patron', '0002_alter_missingperson_gender_alter_missingperson_race_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='missingperson',
            old_name='ageAtMissing',
            new_name='age_At_Missing',
        ),
        migrations.RenameField(
            model_name='missingperson',
            old_name='dateMissing',
            new_name='date_Missing',
        ),
        migrations.RenameField(
            model_name='missingperson',
            old_name='firstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='missingperson',
            old_name='lastName',
            new_name='last_name',
        ),
    ]