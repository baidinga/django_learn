# coding:utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    list = []
    list.append(request)
    list.append(u'shabi')
    return HttpResponse(12345)