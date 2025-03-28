# Generated by Django 5.1.3 on 2025-03-27 15:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allergy_alarm_app', '0003_accelerometer_gyroscope_heartrate_temperature_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useridentification',
            name='userID',
        ),
        migrations.AlterField(
            model_name='accelerometer',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allergy_alarm_app.useridentification'),
        ),
        migrations.AlterField(
            model_name='gyroscope',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allergy_alarm_app.useridentification'),
        ),
        migrations.AlterField(
            model_name='heartrate',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allergy_alarm_app.useridentification'),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allergy_alarm_app.useridentification'),
        ),
    ]
