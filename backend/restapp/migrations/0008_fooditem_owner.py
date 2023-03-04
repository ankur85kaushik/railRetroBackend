# Generated by Django 4.1.7 on 2023-03-04 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restapp', '0007_remove_subservice_service_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='fooditems', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
