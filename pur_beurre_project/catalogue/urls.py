from django.conf.urls import url

from . import views

app_name = 'catalogue'

urlpatterns = [
    url(r'^mon-compte/', views.my_page, name='my_page'),
    url(r'^mes-produits/', views.my_products, name='my_products'),
    url(r'mentions-legales/', views.legal_notice, name='legal-notice'),
    url(r'^search/$', views.search, name='search'),
    url(r'^save/<product_id>', views.save_in_db, name='save'),
    url(r'^(?P<product_id>[0-9]+)/$', views.detail, name='detail'),
]
