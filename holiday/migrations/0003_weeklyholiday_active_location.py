# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-22 08:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0006_auto_20161204_1103'),
        ('holiday', '0002_auto_20151116_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='weeklyholiday',
            name='active_location',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='hr.Location'),
        ),
    ]
