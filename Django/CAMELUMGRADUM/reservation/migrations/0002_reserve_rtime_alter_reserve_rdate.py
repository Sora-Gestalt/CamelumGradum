# Generated by Django 5.0.2 on 2024-03-14 09:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserve',
            name='RTime',
            field=models.TimeField(default=datetime.datetime(2024, 3, 14, 9, 40, 47, 814270, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='reserve',
            name='RDate',
            field=models.DateField(),
        ),
    ]
