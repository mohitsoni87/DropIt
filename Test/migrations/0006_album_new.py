# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0005_remove_album_album_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='new',
            field=models.CharField(max_length=100, null=True),
        ),
    ]