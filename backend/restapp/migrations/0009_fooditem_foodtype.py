# Generated by Django 4.1.7 on 2023-03-04 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0008_fooditem_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='foodtype',
            field=models.CharField(default='veg', max_length=20),
        ),
    ]
