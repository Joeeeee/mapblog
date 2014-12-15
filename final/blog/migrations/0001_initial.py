# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addfriend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('friendid', models.CharField(max_length=5)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2014, 12, 15, 9, 36, 5, 798107))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=300)),
                ('latitude', models.DecimalField(max_digits=10, decimal_places=3)),
                ('longitude', models.DecimalField(max_digits=10, decimal_places=3)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2014, 12, 15, 9, 36, 5, 795986))),
                ('blog_comment_count', models.CharField(default=b'0', max_length=10)),
                ('blog_like_count', models.CharField(default=b'0', max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2014, 12, 15, 9, 36, 5, 796617))),
                ('type', models.CharField(default=b'1', max_length=5)),
                ('content', models.CharField(max_length=300)),
                ('blogid', models.ForeignKey(to='blog.Blog')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('friendid', models.CharField(max_length=5)),
                ('remark', models.CharField(max_length=30)),
                ('friend_type', models.CharField(default=b'0', max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'Group', max_length=30)),
                ('member_count', models.CharField(default=b'0', max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Groupmember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('test222', models.CharField(max_length=1)),
                ('groupid', models.ForeignKey(to='blog.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=5)),
                ('isread', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo1', models.FileField(upload_to=b'./static/Upload/Photo')),
                ('photo2', models.FileField(upload_to=b'./static/Upload/Photo')),
                ('photo3', models.FileField(upload_to=b'./static/Upload/Photo')),
                ('photo4', models.FileField(upload_to=b'./static/Upload/Photo')),
                ('photo5', models.FileField(upload_to=b'./static/Upload/Photo')),
                ('photo6', models.FileField(upload_to=b'./static/Upload/Photo')),
                ('photo7', models.FileField(upload_to=b'./static/Upload/Photo')),
                ('photo8', models.FileField(upload_to=b'./static/Upload/Photo')),
                ('photo9', models.FileField(upload_to=b'./static/Upload/Photo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=16)),
                ('info', models.CharField(max_length=300)),
                ('head', models.FileField(upload_to=b'./static/Upload/Head')),
                ('nickname', models.CharField(max_length=30)),
                ('last_longitude', models.DecimalField(null=True, max_digits=10, decimal_places=7)),
                ('last_latitude', models.DecimalField(null=True, max_digits=10, decimal_places=7)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='message',
            name='userid',
            field=models.ForeignKey(to='blog.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='groupmember',
            name='userid',
            field=models.ForeignKey(to='blog.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='userid',
            field=models.ForeignKey(to='blog.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='friend',
            name='userid',
            field=models.ForeignKey(to='blog.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='userid',
            field=models.ForeignKey(to='blog.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blog',
            name='photoid',
            field=models.ForeignKey(to='blog.Photo', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blog',
            name='userid',
            field=models.ForeignKey(to='blog.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='addfriend',
            name='userid',
            field=models.ForeignKey(to='blog.User'),
            preserve_default=True,
        ),
    ]
