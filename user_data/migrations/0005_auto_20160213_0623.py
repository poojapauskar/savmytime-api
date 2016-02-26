# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-13 06:23
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0004_user_data_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='phone',
            field=models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator(message=b"Enter country code. Phone number must be entered in the format: '919999999'.", regex=b'^\\+?1?\\d{12}$')]),
        ),
    ]