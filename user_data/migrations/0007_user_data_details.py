# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-15 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0006_auto_20160213_0712'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_data',
            name='details',
            field=models.TextField(default=b''),
        ),
    ]
