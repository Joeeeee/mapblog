__author__ = 'Joeeee'
#! /usr/bin/env python
# -*- coding: utf-8 -*-

# URLconf
from django.conf.urls import patterns, url

from blog import views
urlpatterns = patterns("",

    # test for connect
    url(r'^hello$', views.helloworld, name='helloworld'),

    # test for main page
    url(r'^main$', views.main, name='main'),

    # user register
    # POST
    # phone, password, sex, nickname
    url(r'^register', views.register, name='register'),

    # user login
    # POST
    # phone, password
    url(r'^login', views.login,name='login'),

    # user send a addfriend request
    # POST
    # userid, receiver id
    url(r'^addfriend', views.add_friend,name='addfriend'),

    # user confirm an add friend request
    # POST
    # userid, friendid, type, addfirendid
    url(r'^confirm', views.confirm_add_friend,name='confirm_add_friend'),

    # user publish a blog
    # POST
    # content, longitude, latitude, userid
    url(r'^publish', views.publish_blog,name='publish_blog'),

    # # user upload head photo
    # url(r'^testfile',views.testfile,name='testfile'),

    )