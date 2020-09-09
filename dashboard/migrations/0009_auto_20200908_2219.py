# Generated by Django 3.0.7 on 2020-09-08 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_loansettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loans',
            name='status',
            field=models.ForeignKey(default='unpaid', on_delete=django.db.models.deletion.CASCADE, to='dashboard.LoanStatus'),
        ),
    ]