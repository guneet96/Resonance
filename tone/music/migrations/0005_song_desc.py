# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-15 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_song_e_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='desc',
            field=models.CharField(blank=True, max_length=600),
        ),
    ]
