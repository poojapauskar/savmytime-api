# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-08 07:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_providers', '0002_auto_20160106_0716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service_providers',
            name='service_id',
        ),
    ]
