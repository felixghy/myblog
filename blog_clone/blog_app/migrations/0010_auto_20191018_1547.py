# Generated by Django 2.2.5 on 2019-10-18 15:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0009_auto_20191018_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 18, 15, 47, 32, 947541, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 18, 15, 47, 32, 946991, tzinfo=utc)),
        ),
    ]