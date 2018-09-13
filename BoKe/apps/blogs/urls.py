# -*- coding: utf-8 -*-
# __author__ = 'ZKL'
# __date__ = '2018/5/5 10:28'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^show/$', views.show, name='show'),
    url(r'^user/$', views.user, name='user'),
    url(r'^poll/$', views.poll, name='poll'),
    url(r'^keep/$', views.keep, name='keep'),
    url(r'^comment/$', views.comment, name='comment'),
    url(r'^update/$', views.update, name='update'),


]