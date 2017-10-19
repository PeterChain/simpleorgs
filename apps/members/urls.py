from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin

from .views import *

urlpatterns = [
    url(r'^new/$', MemberCreate.as_view(), name='create'),
    url(r'^list/$', MemberList.as_view(), name='list'),
    url(r'^detail/(?P<member_no>[\w-]+)$', MemberDetail.as_view(), name='detail'),
    url(r'^success/(?P<slug>[\w-]+)/$', SuccessView.as_view(), name='success')
]
