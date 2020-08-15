
# Django
from django.urls import reverse_lazy

# Django REST Framework
from rest_framework.test import APITestCase, APIClient

# Models
from django.contrib.auth.models import User
from users.models import Profile


class UserTestCase(APITestCase):

    def setUp(self):
        self.url_register = reverse_lazy('users:register_user')

        self.user1 = User.objects.create(username='cristhian', email='user1@gmail.com', password='user123')
        Profile.objects.create(user=self.user1)

        self.user2 = User.objects.create(username='camila', email='user2@gmail.com', password='user123')
        Profile.objects.create(user=self.user2)

        self.url_follow_user = reverse_lazy('users:user-follow', kwargs={'username': self.user2.username})
        self.url_unfollow_user = reverse_lazy('users:user-unfollow', kwargs={'username': self.user2.username})

        self.client1 = APIClient()

        self.data = {
            'username': 'bycristhian',
            'email': 'bycristhian@gmail.com',
            'password': 'bycristhian123'
        }

    def test_register_user(self):
        response = self.client.post(self.url_register, data=self.data, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.all().count(), 3)


    def test_username_already_exists(self):
        response1 = self.client.post(self.url_register, data=self.data, format='json')
        response2 = self.client.post(self.url_register, data=self.data, format='json')

        self.assertEqual(response1.status_code, 201)
        self.assertEqual(response2.status_code, 400)
        self.assertEqual(User.objects.all().count(), 3)


    def test_follow_user(self):
        self.client1.force_authenticate(user=self.user1)
        response = self.client1.put(self.url_follow_user)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.user1.profile.follows.all().count(), 1)


    def test_unfollow_user(self):
        self.client1.force_authenticate(user=self.user1)
        self.client1.put(self.url_follow_user)
        response = self.client1.put(self.url_unfollow_user)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.user1.profile.follows.all().count(), 0)


    def test_follow_repeat(self):
        self.client1.force_authenticate(user=self.user1)
        response1 = self.client1.put(self.url_follow_user)
        response2 = self.client1.put(self.url_follow_user)

        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 400)
        



