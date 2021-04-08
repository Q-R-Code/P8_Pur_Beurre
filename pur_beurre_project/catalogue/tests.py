from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.test import TestCase
from django.urls import reverse

from .models import Product, Sub_saved


class TestViews(TestCase):
    """Test some views"""

    def test_index_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogue/index.html')

    def test_legal_view(self):
        response = self.client.get(reverse('catalogue:legal-notice'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogue/legal-notice.html')


class TestProducts(TestCase):

    def setUp(self):
        Product.objects.create(
            name="Produit1",
            image_url="https://produit1-image-url.fr",
            categories=['Boissons', 'Eaux', 'breakfasts'],
            nutriscore_grade="b",
            image_nutriments="https://produit1-nutriments.fr",
            barcode="3274080011111",
            url="https://produit1-url.fr"
        ).save()
        Product.objects.create(
            name="Produit2",
            image_url="https://produit2-image-url.fr",
            categories="[Boissons, Eaux, breakfasts]",
            nutriscore_grade="b",
            image_nutriments="https://produit2-nutriments.fr",
            barcode="3274080022222",
            url="https://produit2-url.fr"
        ).save()
        User.objects.create(username="user1", email="user1@user1.com", password="azerty").save()
        self.user1 = User.objects.get(username="user1")
        self.product1 = Product.objects.get(name="Produit1")
        self.product2 = Product.objects.get(name="Produit2")

    def test_search_view_none(self):
        response = self.client.get(reverse('catalogue:search'))
        self.assertEquals(response.status_code, 302, "Vous n'avez rien saisi")
        self.assertTemplateUsed(redirect('index.html'))

    def test_search_view_good(self):
        response = self.client.get(reverse('catalogue:search'), {'query': 'Product1'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogue/search.html')

    def test_search_view_bad(self):
        response = self.client.get(reverse('catalogue:search'), {'query': 'Badname'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogue/search.html')

    def test_detail_view(self):
        product_id = self.product1.id
        response = self.client.get(reverse('catalogue:detail', args=[product_id]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogue/detail.html')

    def test_save_sub_db(self):
        self.client.force_login(self.user1)
        sub_id = self.product1.id
        old_sub = Sub_saved.objects.count()
        response = self.client.post(reverse('catalogue:save', args=[sub_id]))
        new_sub = Sub_saved.objects.count()
        self.assertEquals(new_sub, old_sub + 1)

    def test_delete_sub_db(self):
        self.client.force_login(self.user1)
        Sub_saved.objects.create(user_id=self.user1.id, sub_id=self.product1.id).save()
        sub_id = self.product1.id
        old_sub = Sub_saved.objects.count()
        response = self.client.post(reverse('catalogue:delete', args=[sub_id]))
        new_sub = Sub_saved.objects.count()
        self.assertEquals(new_sub, old_sub - 1)
