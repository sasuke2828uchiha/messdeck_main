# Generated by Django 4.2.7 on 2023-11-17 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='staff_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=30)),
                ('staff_mess', models.CharField(max_length=10)),
            ],
        ),
    ]
