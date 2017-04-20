# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 12:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
        ('manager', '0002_auto_20170316_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='vm',
            name='schedule',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='scheduler.Schedules'),
        ),
    ]
