# Generated by Django 4.2.7 on 2023-11-24 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studeck', '0003_alter_feedbacks_feed_back'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbacks',
            name='picture',
            field=models.ImageField(blank=True, upload_to='feedback_pics/'),
        ),
    ]
