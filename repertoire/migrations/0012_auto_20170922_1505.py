# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-22 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repertoire', '0011_auto_20170922_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oeuvre',
            name='auteur',
        ),
        migrations.AddField(
            model_name='oeuvre',
            name='auteur2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
