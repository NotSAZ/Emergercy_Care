# Generated by Django 5.0.3 on 2024-05-12 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Location', '0012_delete_viewer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icuvacancy',
            name='Vacancy',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
