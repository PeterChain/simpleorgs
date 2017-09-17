from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin

from .views import *

urlpatterns = [
    url(r'^book/$', AddressBookListView.as_view(), name='book'),
]
