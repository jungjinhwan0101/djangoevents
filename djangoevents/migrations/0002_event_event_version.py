# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-06 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoevents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_version',
            field=models.IntegerField(null=True),
        ),
    ]
