#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

import base.util as utils
from expert.models import MC, MakeUp

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def price_filter(query_set):
    kwargs = dict()
    bottom, top = query_set.get('price', '-').split('-')

    if bottom:
        kwargs['price__gte'] = bottom

    if top:
        kwargs['price__lte'] = top

    return kwargs


def expert_filter(query_set, url, obj):
    kwargs = price_filter(query_set)

    def add_para(db, para):
        value = query_set.get(para, 'all')
        if value != 'all':
            kwargs['%s__in' % db] = (value, 'all')

    for para in utils.get_filter_names('expert'):
        add_para(para, para)

    content = {
        'paras': utils.get_filter_sets('expert'),
        'cart_url': url,
        'data_set': obj.objects.filter(**kwargs),
        }

    return content


def filter_mc(request):
    content = expert_filter(request.GET, 'add_service_mc', MC)
    return render_to_response('mc.html', RequestContext(request, content))


def filter_makeup(request):
    content = expert_filter(request.GET, 'add_service_makeup', MakeUp)
    return render_to_response('makeup.html', RequestContext(request, content))
