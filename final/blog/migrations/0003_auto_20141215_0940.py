# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20141215_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.CharField(default=b'20', max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='addfriend',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 15, 9, 40, 53, 295062)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 15, 9, 40, 53, 292825)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 15, 9, 40, 53, 293446)),
            preserve_default=True,
        ),
    ]
