# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-24 09:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0005_user_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='players', to='football.User'),
        ),
    ]
