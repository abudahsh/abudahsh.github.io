# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-26 14:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0017_auto_20171226_1550'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentreport',
            old_name='examrecrods',
            new_name='examrecords',
        ),
    ]
