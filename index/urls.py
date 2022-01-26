# -*- encoding:utf-8 -*-
# author: liuheng
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index')
]