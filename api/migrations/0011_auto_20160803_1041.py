# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-03 10:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20160803_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='influence',
            name='journal',
        ),
        migrations.DeleteModel(
            name='Influence',
        ),
    ]
