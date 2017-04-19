# -*- coding: utf-8 -*-
from django.conf.urls import url

from myproject.myapp import views
from django.conf.urls.static import static

urlpatterns = [

    url(r'^$', views.home, name='home'),
]

