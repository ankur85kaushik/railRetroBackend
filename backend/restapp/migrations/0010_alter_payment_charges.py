# Generated by Django 4.1.7 on 2023-03-04 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0009_fooditem_foodtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='charges',
            field=models.IntegerField(blank=True),
        ),
    ]
