# Generated by Django 4.1 on 2023-01-18 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0062_scheduling_delete_ress'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduling',
            name='can_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
