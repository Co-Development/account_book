# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    File Name :     urls
    Author :        snail
    date :          2018/12/9
-------------------------------------------------
    Description : 
-------------------------------------------------
"""
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('bills/', views.bill_list, name='bills'),
    path('bills/id/<int:bi_id>/', views.bills_id, name='bills_for_id'),

    path('bills/<int:bd_year>/', views.bills_date, name='bills_for_date'),
    re_path('bills/(?P<bd_year>\d{4})/$', views.bills_date, name='bills_for_date'),
    re_path('bills/(?P<bd_year>\d{4})/(?P<bd_mon>\d{1,2})/$', views.bills_date, name='bills_for_date'),
    re_path('bills/(?P<bd_year>\d{4})/(?P<bd_mon>\d{1,2})/(?P<bd_day>\d{1,2})/$', views.bills_date,
            name='bills_for_date'),
    path('bills/<str:bn_name>/', views.bills_name, name='bills_for_name'),

    path('add/', views.bill_add, name='bill_add'),
    path('delete/<id>', views.bill_delete, name='bill_delete'),
    path('update/', views.bill_update, name='bill_update'),
]
