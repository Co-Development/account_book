# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    File Name :     urls
    Author :        snail
    date :          2018/12/11
-------------------------------------------------
    Description : 
-------------------------------------------------
"""
from django.urls import path, re_path

from .models import ExpensesNotes, User
from . import views

expenses_notes_views = views.CusViews(ExpensesNotes)
user_views = views.CusViews(User)

urlpatterns = [
    path('notes/', expenses_notes_views.model_all, name='notes_all'),
    path('note/query/id/<int:ni_id>/', expenses_notes_views.model_id, name='notes_for_id'),
    re_path('notes/query/(?P<nd_year>\d{4})/$', views.notes_for_date, name='notes_for_date'),
    re_path('notes/query/(?P<nd_year>\d{4})/(?P<nd_mon>\d{1,2})/$', views.notes_for_date,
            name='notes_for_date'),
    re_path('notes/query/(?P<nd_year>\d{4})/(?P<nd_mon>\d{1,2})/(?P<nd_day>\d{1,2})/$',
            views.notes_for_date, name='notes_for_date'),
    path('notes/query/<str:nn_name>/', views.notes_for_username, name='notes_for_name'),
    path('note/save/', expenses_notes_views.save_model, name='save_note'),
    path('note/update/', expenses_notes_views.update_model, name='update_notes'),

    path('users/query/id/<int:ni_id>/', user_views.model_all, name='user_all'),
    path('user/save/', user_views.save_model, name='save_user'),
    path('user/update/', user_views.update_model, name='update_user'),
]
