from django.conf.urls import url

from . import views

app_name = 'catalogue'

urlpatterns = [
    url(r'^mon-compte/', views.my_page, name='my_page'),
    url(r'^mes-produits/', views.my_products, name='my_products')
]
