from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from catalogue import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^catalogue/', include('catalogue.urls', namespace='catalogue')),
    url(r'^admin/', admin.site.urls),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns