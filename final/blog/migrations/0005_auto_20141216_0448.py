# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20141215_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='sendid',
            field=models.CharField(default='Null', max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='addfriend',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 16, 4, 48, 22, 426429)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 16, 4, 48, 22, 424193)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 16, 4, 48, 22, 424809)),
            preserve_default=True,
        ),
    ]
