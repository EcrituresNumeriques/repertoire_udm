# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-21 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repertoire', '0002_auto_20170921_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='Oeuvre',
            name='lieu',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='Oeuvre',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]