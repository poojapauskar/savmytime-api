# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-15 07:20
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0009_remove_user_data_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_data',
            name='detail_array',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, default=b''), default=django.utils.timezone.now, size=None),
            preserve_default=False,
        ),
    ]
