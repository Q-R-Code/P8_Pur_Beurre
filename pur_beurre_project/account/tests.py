from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class TestAccountViews(TestCase):
    """Test some views"""

    def setUp(self):
        User.objects.create(username="user1", email="user1@user1.com", password="azerty").save()
        self.user1 = User.objects.get(username="user1")

    #Test la view de inscription renvoie 200
    def test_register_view(self):
        response = self.client.get(reverse('account:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/register.html')

    #Test l'inscription d'un user marche
    #Test l'inscirption d'un user avec une erreur

    #Test la vue de connection 200
    def test_connection_view(self):
        response = self.client.get(reverse('account:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    #Test la connection d'un user marche
    #Test la connection avec une erreur


