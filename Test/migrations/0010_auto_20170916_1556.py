# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-16 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0009_song_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(max_length=1000, null=True, upload_to=b''),
        ),
    ]