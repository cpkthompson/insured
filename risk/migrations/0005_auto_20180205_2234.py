# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-05 22:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk', '0004_auto_20180205_2207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comprehensivetarif',
            old_name='total_basic_premiums',
            new_name='total_basic_premium',
        ),
        migrations.RenameField(
            model_name='comprehensivetarif',
            old_name='total_basic_premiums_currency',
            new_name='total_basic_premium_currency',
        ),
        migrations.RenameField(
            model_name='thirdpartytarif',
            old_name='total_basic_premiums',
            new_name='total_basic_premium',
        ),
        migrations.RenameField(
            model_name='thirdpartytarif',
            old_name='total_basic_premiums_currency',
            new_name='total_basic_premium_currency',
        ),
    ]
