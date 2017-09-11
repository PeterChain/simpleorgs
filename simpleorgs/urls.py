from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin

import apps.main.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', apps.main.views.Homepage.as_view(), name='homepage')
]
