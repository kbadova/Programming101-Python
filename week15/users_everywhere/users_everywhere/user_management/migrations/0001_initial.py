# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-09 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.CharField(max_length=140, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=140)),
            ],
        ),
    ]
