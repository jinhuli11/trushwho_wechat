# coding: utf-8
'''
Created on 2016年5月5日

@author: likun
'''
from django.conf.urls import url
from feedback.views import FeedBackCreateView
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', FeedBackCreateView.as_view(), name='feedback'),
    url(r'success/$', TemplateView.as_view(template_name='feedback/success.html'), name='feedback_success'),
]
