# Generated by Django 4.1.7 on 2023-03-04 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0006_order_remove_feedback_job_delete_job_feedback_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subservice',
            name='service',
        ),
        migrations.DeleteModel(
            name='CityServiceSubservice',
        ),
        migrations.DeleteModel(
            name='MyService',
        ),
        migrations.DeleteModel(
            name='SubService',
        ),
    ]
