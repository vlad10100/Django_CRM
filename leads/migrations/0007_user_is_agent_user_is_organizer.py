# Generated by Django 4.0.1 on 2022-01-21 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0006_remove_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_organizer',
            field=models.BooleanField(default=True),
        ),
    ]
