# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-05 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0008_auto_20180205_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='age',
            field=models.CharField(choices=[('one', '1 to 5 years'), ('above', 'Above 10 years'), ('five', '5 to 10 years')], max_length=50),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='cubic_capacity',
            field=models.CharField(choices=[('up_to_1600', 'Up to 1600'), ('1600_to_2000', '1600 to 2000'), ('Above_2000', 'Above 2000')], max_length=50),
        ),
    ]
