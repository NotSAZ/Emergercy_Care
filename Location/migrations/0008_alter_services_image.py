# Generated by Django 5.0.3 on 2024-04-19 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Location', '0007_alter_hospital_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='image',
            field=models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images/'),
        ),
    ]