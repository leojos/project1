# Generated by Django 4.1 on 2023-02-17 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0085_delete_ress_remove_internship_openings'),
    ]

    operations = [
       
        migrations.AddField(
            model_name='internship',
            name='tim',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
