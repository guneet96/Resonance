# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-02 21:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20170215_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='artist',
        ),
    ]
