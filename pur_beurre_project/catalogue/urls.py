from django.conf.urls import url

from . import views

app_name = 'catalogue'

urlpatterns = [
    url(r'^inscription/$', views.account, name='register')
]
