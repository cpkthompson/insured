# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-05 22:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('risk', '0003_auto_20180205_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='comprehensivetarif',
            name='risk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='risk.Risk'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thirdpartytarif',
            name='risk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='risk.Risk'),
            preserve_default=False,
        ),
    ]
