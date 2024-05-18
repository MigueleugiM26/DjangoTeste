# Generated by Django 5.0.6 on 2024-05-18 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_home_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='guest_canPause',
        ),
        migrations.RemoveField(
            model_name='home',
            name='votes_skip',
        ),
        migrations.AddField(
            model_name='home',
            name='mistakes',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='home',
            name='spaces',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='home',
            name='tips',
            field=models.BooleanField(default=True),
        ),
    ]
