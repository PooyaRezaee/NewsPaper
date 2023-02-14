from django.test import SimpleTestCase
from django.urls import reverse

class SignupPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/account/signup/")
        self.assertEqual(response.status_code, 200)

class LoginPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/account/login/")
        self.assertEqual(response.status_code, 200)