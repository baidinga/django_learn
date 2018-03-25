#coding:utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))
def add2(request,a,b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
def change_text(request):
    a = request.GET['text'].encode('utf-8')
    print(a.decode())
    return HttpResponse(a)
def index(request):
    return render(request, 'home.html')

def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )