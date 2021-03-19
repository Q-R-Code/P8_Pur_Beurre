from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):

    name = models.CharField(max_length=200)
    image_url = models.URLField()
    categories = models.CharField(max_length=500)
    nutrition_grade = models.CharField(max_length=5)
    image_nutriments = models.URLField(max_length=1500)
    barcode = models.CharField(max_length=30)

class Sub_saved(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

#https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=unique_scans_n&&page_size=100&json=true