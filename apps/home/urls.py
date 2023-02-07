# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page 
    path('', views.index, name='home'),
    # path('index.html', views.index, name='home'),
    path('komatsu', views.index_komatsu, name='komatsu'),

    #mine 
    path('ajax/update_chart', views.update_chart, name='update_chart'),
    
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

    

]
