# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views

urlpatterns = [
    # == \ main page
    url(r'^$', views.index, name='index'),
]