# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-13 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0009_leavecategory_leave_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='leavecategory',
            name='entitled',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='leavecategory',
            name='forward_validity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='leavecategory',
            name='holiday_skip',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='leavecategory',
            name='is_forward',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='leavecategory',
            name='minimumdays',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='leavecategory',
            name='pre_condition',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='leavecategory',
            name='validity',
            field=models.IntegerField(default=0),
        ),
    ]