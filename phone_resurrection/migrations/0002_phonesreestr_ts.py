# Generated by Django 4.0.1 on 2022-01-29 13:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('phone_resurrection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonesreestr',
            name='ts',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
