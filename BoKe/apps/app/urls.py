# -*- coding: utf-8 -*-
# __author__ = 'ZKL'
# __date__ = '2018/5/5 10:23'

from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^login/$', views.logins, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^active/(?P<code>\w+)$', views.active, name='active'),
]