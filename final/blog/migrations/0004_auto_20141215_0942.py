# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20141215_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addfriend',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 15, 9, 42, 14, 741201)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 15, 9, 42, 14, 738987)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 15, 9, 42, 14, 739595)),
            preserve_default=True,
        ),
    ]
