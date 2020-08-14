
# Django
from django.urls import reverse_lazy

# Django REST Framework
from rest_framework.test import APITestCase

# Models
from django.contrib.auth.models import User


class UserTestCase(APITestCase):

    def setUp(self):
        self.url_register = reverse_lazy('users:register_user')
        self.data = {
            'username': 'bycristhian',
            'email': 'bycristhian@gmail.com',
            'password': 'bycristhian123'
        }

    def test_register_user(self):
        response = self.client.post(self.url_register, data=self.data, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.all().count(), 1)


    def test_username_already_exists(self):
        response1 = self.client.post(self.url_register, data=self.data, format='json')
        response2 = self.client.post(self.url_register, data=self.data, format='json')

        self.assertEqual(response1.status_code, 201)
        self.assertEqual(response2.status_code, 400)
        self.assertEqual(User.objects.all().count(), 1)

