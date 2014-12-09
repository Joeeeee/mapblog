__author__ = 'Joeeee'
#! /usr/bin/env python
# -*- coding: utf-8 -*-

# URLconf
from django.conf.urls import patterns, url

from blog import views
urlpatterns = patterns("",
    url(r'^hello$',views.helloworld,name='helloworld'),
    url(r'^sign_in',views.sign_in,name='sign_in'),

    )