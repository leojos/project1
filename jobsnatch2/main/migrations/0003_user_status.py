# Generated by Django 4.1 on 2022-08-24 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.BooleanField(default=0, verbose_name='status'),
        ),
    ]
