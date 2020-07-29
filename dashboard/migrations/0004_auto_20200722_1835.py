# Generated by Django 3.0.7 on 2020-07-22 18:35

import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20200722_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamamembers',
            name='memberID',
            field=models.CharField(default=dashboard.models.generate_memberID, max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transactionID',
            field=models.CharField(default=dashboard.models.generate_TransactionID, max_length=20, primary_key=True, serialize=False),
        ),
    ]