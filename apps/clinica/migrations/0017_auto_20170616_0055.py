# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-06-16 00:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0016_auto_20170615_2210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mascota',
            old_name='dueño',
            new_name='duenho',
        ),
    ]
