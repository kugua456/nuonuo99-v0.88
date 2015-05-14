#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

from service.models import MC, MakeUp, S_Flower

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def expert_filter(query_set):
    kwargs = dict()

    # gender filter
    gender = query_set.get('gender', '0')
    if gender != '0':
        kwargs['gender'] = gender

    return kwargs


def filter_makeup(request):
    kwargs = expert_filter(request.GET)
    content = {
        'data_set': MakeUp.objects.filter(**kwargs),
            }
    return render_to_response('makeup.html', RequestContext(request, content))


def filter_mc(request):
    kwargs = expert_filter(request.GET)
    content = {
        'data_set': MC.objects.filter(**kwargs),
            }
    return render_to_response('mc.html', RequestContext(request, content))


def filter_flower(request):
    kwargs = dict()
    content = {
        'data_set': S_Flower.objects.filter(**kwargs),
        }
    return render_to_response('flower.html', RequestContext(request, content))
