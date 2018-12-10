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
from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.bill_list, name='bill_list'),
    path('add/', views.bill_add, name='bill_add'),
    path('delete/', views.bill_delete, name='bill_delete'),
    path('update/', views.bill_update, name='bill_update'),
]
