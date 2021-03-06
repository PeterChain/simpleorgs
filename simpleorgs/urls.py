from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin

import apps.main.views
import apps.address.urls
import apps.members.urls
import apps.main.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', apps.main.views.Homepage.as_view(), name="homepage"),
    url(r'^login/', apps.main.views.LoginView.as_view(), name="login"),
    url(r'^logout/', apps.main.views.LogoutView.as_view(), name="logout"),
    url(r'^settings/', apps.main.views.UserSettingsView.as_view(), name="settings"),
    url(r'^member/', include(apps.members.urls, namespace="members")),
    url(r'^address/', include(apps.address.urls, namespace="address"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)