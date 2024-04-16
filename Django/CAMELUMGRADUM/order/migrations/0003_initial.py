# Generated by Django 5.0.2 on 2024-03-07 09:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0002_delete_coffee_bags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee_Bags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CName', models.CharField(max_length=80)),
                ('CBP', models.ImageField(upload_to='')),
                ('CBD', models.TextField(default='Sorry No Description Has Been Added ;-;')),
                ('Country', models.CharField(max_length=56)),
                ('Cdate', models.DateField(default=datetime.date.today)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
    ]
