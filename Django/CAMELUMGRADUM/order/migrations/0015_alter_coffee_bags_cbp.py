# Generated by Django 5.0.2 on 2024-03-07 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_alter_coffee_bags_cbp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee_bags',
            name='CBP',
            field=models.ImageField(upload_to='Coffee-Bags'),
        ),
    ]
