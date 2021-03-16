from django.conf.urls import url

from . import views

app_name = 'account'

urlpatterns = [
    url(r'^inscription/', views.register, name='register'),
    url(r'^connection/', views.login, name='login'),
]