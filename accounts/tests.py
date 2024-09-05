from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
from django.urls import reverse


class SignUpAccountTes(TestCase):
    def test_sign_up_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual( response.status_code, 200)

    def test_sign_up_by_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)


