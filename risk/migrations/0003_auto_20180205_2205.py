# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-05 22:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk', '0002_auto_20180205_2204'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ThirdPartyTarifs',
            new_name='ComprehensiveTarif',
        ),
        migrations.RenameModel(
            old_name='ComprehensiveTarifs',
            new_name='ThirdPartyTarif',
        ),
    ]
