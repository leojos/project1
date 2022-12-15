# Generated by Django 4.1 on 2022-09-12 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_user_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(null=True, upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='cat',
            field=models.CharField(choices=[('null', 'null'), ('Programming and Tech', 'Programming and Tech'), ('Accounting and Finance', 'Accounting and Finance'), ('Data Science and Analytics', 'Data Science and Analytics'), ('Writing \\ Translation', 'Writing \\ Translation'), ('Education \\ Training', 'Education \\ Training'), ('Restaurant \\ Food Service', 'Restaurant \\ Food Service'), ('Design,Art and Multimedia', 'Design,Art and Multimedia'), ('Sales \\ Markeing', 'Sales \\ Markeing')], default=0, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='is_admin'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_candidate',
            field=models.BooleanField(default=False, verbose_name='is_candidate'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_company',
            field=models.BooleanField(default=False, verbose_name='is_company'),
        ),
    ]
