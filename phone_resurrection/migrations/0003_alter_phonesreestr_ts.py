# Generated by Django 4.0.1 on 2022-01-29 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone_resurrection', '0002_phonesreestr_ts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonesreestr',
            name='ts',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
