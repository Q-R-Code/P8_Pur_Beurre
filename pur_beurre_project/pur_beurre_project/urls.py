from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from catalogue import views



urlpatterns = [
    url(r'^$', views.index),
    url(r'^catalogue/', include('catalogue.urls', namespace='catalogue')),
    url(r'^compte/', include('account.urls', namespace='account')),
    url(r'^pur-beurre-staff/', admin.site.urls),
    url('', include("django.contrib.auth.urls"))

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns