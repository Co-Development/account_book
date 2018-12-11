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
import calendar
import json
from datetime import datetime

from django.http import JsonResponse

from accountbook.models import ExpensesNotes

base_response = {
    'success': True,
    'data': [],
    'msg': '',
}


# Create your views here.
class CusViews(object):
    def __init__(self, _model):
        self.model = _model

    def model_all(self, request):
        bi_response = base_response

        offset = request.GET.get('offset', 1)
        limit = request.GET.get('limit', 50)

        bi_response['data'] = list(self.model.objects.all()[offset - 1:limit].values())
        return JsonResponse(bi_response)
    
    def model_id(self, request, ni_id):
        ni_response = base_response
        ni_response['msg'] = f'for id: {ni_id}'
        ni_response['data'] = self.model.objects.get(id=ni_id).to_dict()
        return JsonResponse(ni_response, safe=False)

    def save_model(self, request):
        sn_response = base_response
        received_json_data = json.loads(request.body.decode())
        expenses__model = self.model(**received_json_data)
        expenses__model.save()
        sn_response['msg'] = 'save'
        return JsonResponse(sn_response)

    def update_model(self, request):
        un_response = base_response
        received_json_data = json.loads(request.body)
        if 'id' not in received_json_data:
            un_response['success'] = False
            un_response['msg'] = '缺少ID'
            un_response.pop('data')
            return JsonResponse(un_response)
        success_num = self.model.objects.filter(id=received_json_data['id']).update(**received_json_data)
        un_response['msg'] = 'update'
        un_response['data'] = success_num
    
        return JsonResponse(un_response)


def notes_all(self, request):
    bi_response = base_response

    offset = request.GET.get('offset', 1)
    limit = request.GET.get('limit', 50)

    bi_response['data'] = list(self.model.objects.all().order_by('-create_time')[offset - 1:limit].values())
    return JsonResponse(bi_response)


def notes_for_date(request, nd_year=2018, nd_mon=0, nd_day=0):
    offset = request.GET.get('offset', 1)
    limit = request.GET.get('limit', 50)

    nd_year, nd_mon, nd_day = [int(nd_year), int(nd_mon), int(nd_day)]

    nd_response = base_response

    if nd_day:
        nd_response['msg'] = 'for createTime'
        start_date = datetime(nd_year, nd_mon, nd_day)
        end_date = datetime(nd_year, nd_mon, nd_day, 23, 59, 59)
        nd_response['data'] = list(ExpensesNotes.objects.filter(create_time__range=(start_date, end_date)).values())
    else:
        if nd_mon:
            nd_response['msg'] = 'for createTime in mon'
            start_date = datetime(nd_year, nd_mon, 1)
            _, month_range = calendar.monthrange(nd_year, nd_mon)
            end_date = datetime(nd_year, nd_mon, month_range, 23, 59, 59)
            nd_response['data'] = list(
                ExpensesNotes.objects.filter(create_time__range=(start_date, end_date))[offset - 1:limit].values())
        else:
            nd_response['msg'] = 'for createTime in year'
            nd_response['data'] = list(
                ExpensesNotes.objects.filter(create_time__year=nd_year)[offset - 1:limit].values())
    return JsonResponse(nd_response)


def notes_for_username(request, user_name):
    offset = request.GET.get('offset', 1)
    limit = request.GET.get('limit', 50)

    nn_response = base_response
    nn_response['msg'] = 'for name: ' + user_name

    nn_response['data'] = list(ExpensesNotes.objects.filter(user__name=user_name)[offset - 1:limit].values())
    return JsonResponse(nn_response)
