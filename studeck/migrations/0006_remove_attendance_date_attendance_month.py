# Generated by Django 4.2.7 on 2023-11-27 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studeck', '0005_attendance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='date',
        ),
        migrations.AddField(
            model_name='attendance',
            name='month',
            field=models.IntegerField(default=0),
        ),
    ]
