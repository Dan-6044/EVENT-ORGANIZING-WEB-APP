# Generated by Django 5.1.4 on 2025-04-08 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizers', '0003_alter_transportation_transport_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transportation',
            name='passenger_capacity',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='transportation',
            name='special_requests',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='transportation',
            name='transport_schedule',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
