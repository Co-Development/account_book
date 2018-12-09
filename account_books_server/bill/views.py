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
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

base_response = {
    'success': True,
    'data': [],
    'msg': '',
}


def bill_list(request):
    return JsonResponse(base_response)


def bill_add(request):
    return JsonResponse(base_response)


def bill_delete(request):
    return JsonResponse(base_response)


def bill_update(request):
    return JsonResponse(base_response)
