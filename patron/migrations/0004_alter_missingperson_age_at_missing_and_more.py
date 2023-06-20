# Generated by Django 4.2.2 on 2023-06-20 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patron', '0003_rename_ageatmissing_missingperson_age_at_missing_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missingperson',
            name='age_At_Missing',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='missingperson',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patron.gender'),
        ),
        migrations.AlterField(
            model_name='missingperson',
            name='race',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patron.race'),
        ),
        migrations.AlterField(
            model_name='missingperson',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patron.state'),
        ),
    ]
