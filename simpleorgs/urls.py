from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin

import apps.main.views
import apps.address.urls
import apps.members.urls
import apps.main.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', apps.main.views.Homepage.as_view(), name='homepage'),
    url(r'^member/', include(apps.members.urls, namespace="members")),
    url(r'^address/', include(apps.address.urls, namespace="address"))
]
