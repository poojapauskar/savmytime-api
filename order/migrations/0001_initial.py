# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-15 05:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('order_id', models.CharField(default=b'', max_length=100)),
                ('user_id', models.CharField(default=b'', max_length=100)),
                ('status', models.CharField(default=b'', max_length=100)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
