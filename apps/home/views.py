# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import FurnanceData, Accelerations

from django.http import JsonResponse



from django.shortcuts import render
import subprocess


@login_required(login_url="/login/")
def index(request):
    # username = request.user.username
    # by me
    data = FurnanceData.objects.values('date','temperature','current','voltage')
    data2 = Accelerations.objects.values('date','accelx','accely','accelz')

    array_temp = [[term['date'].timestamp()*1000, term['temperature']] for term in data]
    array_curr= [[term['date'].timestamp()*1000, term['current']] for term in data]
    array_vol = [[term['date'].timestamp()*1000, term['voltage']] for term in data]

    array_accelx = [[term['date'].timestamp()*1000, term['accelx']] for term in data2]
    array_accely= [[term['date'].timestamp()*1000, term['accely']] for term in data2]
    array_accelz = [[term['date'].timestamp()*1000, term['accelz']] for term in data2]


    #


    context = {'segment': 'index',
                'array_temp':array_temp,
                'array_curr':array_curr,
                'array_vol':array_vol,
                'array_accelx': array_accelx,
                'array_accely': array_accely,
                'array_accelz': array_accelz,
                }

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
def index_komatsu(request):
    # by me
    data = FurnanceData.objects.values('date','temperature','current','voltage')
    data2 = Accelerations.objects.values('date','accelx','accely','accelz')

    array_temp = [[term['date'].timestamp()*1000, term['temperature']] for term in data]
    array_curr= [[term['date'].timestamp()*1000, term['current']] for term in data]
    array_vol = [[term['date'].timestamp()*1000, term['voltage']] for term in data]

    array_accelx = [[term['date'].timestamp()*1000, term['accelx']] for term in data2]
    array_accely= [[term['date'].timestamp()*1000, term['accely']] for term in data2]
    array_accelz = [[term['date'].timestamp()*1000, term['accelz']] for term in data2]


    #


    context = {'segment': 'index_komatsu',
                'array_temp':array_temp,
                'array_curr':array_curr,
                'array_vol':array_vol,
                'array_accelx': array_accelx,
                'array_accely': array_accely,
                'array_accelz': array_accelz,
                }

    html_template = loader.get_template('komatsu/home/index.html')
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))



def update_chart(request):
    # getting the last data
    raw_data = FurnanceData.objects.values('date','temperature','current','voltage').latest('id')
    raw_data2 = Accelerations.objects.values('date','accelx','accely','accelz').latest('id')

    data1 = [raw_data['date'].timestamp()*1000, raw_data['temperature']]
    data2 = [raw_data['date'].timestamp()*1000, raw_data['current']]
    data3 = [raw_data['date'].timestamp()*1000, raw_data['voltage']]

    data4 = [raw_data2['date'].timestamp()*1000, raw_data2['accelx']]
    data5 = [raw_data2['date'].timestamp()*1000, raw_data2['accely']]
    data6 = [raw_data2['date'].timestamp()*1000, raw_data2['accelz']]
    data = {              
            'temp_update':data1,
            'curr_update':data2,
            'vol_update':data3,
            'accelx_update':data4,
            'accely_update':data5,
            'accelz_update':data6,
            }
    return JsonResponse(data, safe=False)
