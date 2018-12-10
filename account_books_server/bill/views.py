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
from bill.models import AccountBook

base_response = {
    'success': True,
    'data': [],
    'msg': '',
}


def bill_list(request):
    account_book_all = AccountBook.objects.values()
    base_response['data'] = list(account_book_all)
    return JsonResponse(base_response)


def bills_id(request, bi_id):
    bi_response = base_response
    bi_response['msg'] = 'for id: {}'.format(bi_id)
    return JsonResponse(base_response)


def bills_name(request, bn_name):
    bn_response = base_response
    bn_response['msg'] = 'for create_name: ' + bn_name
    return JsonResponse(bn_response)


def bills_date(request, bd_year=2018, bd_mon=0, bd_day=0):
    bd_response = base_response
    bd_response['msg'] = 'for createTime'
    if not bd_day:
        if not bd_mon:
            bd_response['msg'] = 'for createTime in year'
        else:
            bd_response['msg'] = 'for createTime in mon'
    return JsonResponse(bd_response)


def bill_add(request):
    return JsonResponse(base_response)


def bill_delete(request):
    return JsonResponse(base_response)


def bill_update(request):
    return JsonResponse(base_response)
