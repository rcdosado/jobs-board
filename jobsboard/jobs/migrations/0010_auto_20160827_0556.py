# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 05:56
from __future__ import unicode_literals

from django.db import migrations, models
import jobsboard.common.utils


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_auto_20160820_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='expiry',
        ),
        migrations.AddField(
            model_name='job',
            name='expiry_date',
            field=models.DateField(default=jobsboard.common.utils.get_default_expiry),
        ),
    ]
