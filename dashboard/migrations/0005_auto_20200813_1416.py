# Generated by Django 3.0.7 on 2020-08-13 14:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20200813_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chamas',
            name='funds',
        ),
        migrations.AddField(
            model_name='subscriptions',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='subscriptions',
            name='endDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 20, 14, 16, 22, 473597)),
        ),
    ]