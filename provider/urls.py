#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url


urlpatterns = patterns('provider.views',
    url(r'^(\w+)$', 'provider', name='provider_list'),
)
