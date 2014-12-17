# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20141215_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addfriend',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 17, 12, 47, 31, 817000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 17, 12, 47, 31, 807000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 17, 12, 47, 31, 809000)),
            preserve_default=True,
        ),
    ]
