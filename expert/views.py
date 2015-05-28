#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response

# REST framework
from rest_framework import generics
from rest_framework import permissions

import django_filters

from expert.models import MC, MakeUp
from expert.serializers import McSerializer, MakeUpSerializer

from base.utils import price_filter
import base.choices as choice_set


class McFilter(django_filters.FilterSet):
    price = django_filters.CharFilter(action=choice_set.range_action('price'))
    age = django_filters.CharFilter(action=choice_set.range_action('t_birth'))
    height = django_filters.CharFilter(action=choice_set.range_action('height'))
    mc_tech = django_filters.CharFilter(lookup_type='isnull')

    class Meta:
        model = MC
        fields = ['price', 'wed_sty', 'is_man', 'age', 'height', 'loc_native', 'mc_tech']


class MakeUpFilter(django_filters.FilterSet):
    price = django_filters.CharFilter(action=choice_set.range_action('price'))

    class Meta:
        model = MakeUp
        fields = ['price', 'wed_sty', 'makeup_sty']


def mc_home(request):
    content = {
        'paras': choice_set.MC_PARAS(),
        'list_url': 'mc_list',
        'cart_url': 'add_service_mc',
        'data_set': MC.objects.all(),
        'disp_name': u'司仪',
        }
    return render_to_response('expert.html', RequestContext(request, content))


class McList(generics.ListCreateAPIView):
    queryset = MC.objects.all()
    serializer_class = McSerializer
    filter_class = McFilter


def makeup_home(request):
    content = {
        'paras': choice_set.MAKEUP_PARAS(),
        'list_url': 'makeup_list',
        'cart_url': 'add_service_makeup',
        'data_set': MakeUp.objects.all(),
        'disp_name': u'化妆师',
        }
    return render_to_response('expert.html', RequestContext(request, content))


class MakeUpList(generics.ListCreateAPIView):
    queryset = MakeUp.objects.all()
    serializer_class = MakeUpSerializer
    filter_class = MakeUpFilter
