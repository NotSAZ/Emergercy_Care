# Generated by Django 5.0.3 on 2024-04-13 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Location', '0005_services_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='icuvacancy',
            name='Vacancy',
            field=models.CharField(blank=True, choices=[('Vacant', 'Vacant'), ('Occupied', 'Occupied')], max_length=100, null=True),
        ),
    ]