"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from learn import views as learn_view
from calc import views as calc_view
urlpatterns = [
    url(r'^administration/', admin.site.urls),
    url(r'^learn/', learn_view.index),
    url(r'^add/$', calc_view.index, name='home'),
    url(r'^add/(\d+)/(\d+)/', calc_view.old_add2_redirect),
    url(r'^change/', calc_view.change_text, name='text'),
    url(r'^new_add/(\d+)/(\d+)/', calc_view.add2, name='add2'),
]
