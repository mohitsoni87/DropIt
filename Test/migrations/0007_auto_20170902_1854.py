# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 13:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0006_album_new'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='new',
            new_name='new_column',
        ),
    ]