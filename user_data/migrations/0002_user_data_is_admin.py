# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-06 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_data',
            name='is_admin',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
