# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-15 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='transition_id',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]