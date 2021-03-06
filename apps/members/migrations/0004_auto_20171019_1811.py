# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 17:11
from __future__ import unicode_literals

import apps.members.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20171016_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='has_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='member',
            name='picture',
            field=models.ImageField(upload_to=apps.members.models.get_member_path),
        ),
    ]
