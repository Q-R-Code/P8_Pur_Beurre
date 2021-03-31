from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Sub_saved, Product

class PagesTestCase(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def legal_notice_page(self):
        response = self.client.get(reverse('catalogue:legal-notice'))
        self.assertEqual(response.status_code, 200)


class ProductsTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username="user", password="123456")
        prod1 = Product.objects.create(
            name="Porduit1",
            image_url="https://produit1-image-url.fr",
            categories=["Boissons", "Eaux", "breakfasts"],
            nutriscore_grade= "b",
            image_nutriments="https://produit1-nutriments.fr",
            barcode="3274080005003",
            url="https://produit1-url.fr"
        )
        prod2 = Product.objects.create(
            name="Porduit2",
            image_url="https://produit2-image-url.fr",
            categories=["Boissons", "Eaux", "breakfasts"],
            nutriscore_grade="a",
            image_nutriments="https://produit2-nutriments.fr",
            barcode="3274080005004",
            url="https://produit2-url.fr"
        )
        prod1.save()
        prod2.save()
        self.product1 = Product.objects.get(name="Produit1")
        self.product2 = Product.objects.get(name="Produit2")

    def test_search_page(self):
        query = "Produit1"
        response = self.client.get(reverse('catalogue:search'), {'query': query})
        self.assertEqual(response.status_code, 200)