# Generated by Django 4.2.7 on 2023-11-27 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studeck', '0007_montly_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='total_daily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('breakfast', models.IntegerField(default=0)),
                ('lunch', models.IntegerField(default=0)),
                ('dinner', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='user_total',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('breakfast', models.IntegerField(default=0)),
                ('lunch', models.IntegerField(default=0)),
                ('dinner', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='montly_total',
        ),
    ]
