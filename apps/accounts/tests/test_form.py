from django.test import TestCase
from ..models import User
from django.urls import reverse

class SignupPageTests(TestCase):
    def test_valid_form(self):
        response = self.client.post(
        reverse("account:signup"),
        {
        "username": "testuser",
        "email": "testuser@email.com",
        "age": "18",
        "password1": "testpass123",
        "password2": "testpass123",
        },
        )
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.all().count(), 1)
        self.assertEqual(User.objects.first().username, "testuser")
        self.assertEqual(User.objects.first().email, "testuser@email.com")
        self.assertEqual(User.objects.first().age, 18)
    
    def test_invalid_email(self):
        response = self.client.post(
        reverse("account:signup"),
        {
        "username": "testuser",
        "email": "dwfawdsadsadf",
        "age": "18",
        "password1": "testpass123",
        "password2": "testpass123",
        },
        )

        self.assertEqual(User.objects.all().count(), 0)
    
    def test_not_match_password(self):
        response = self.client.post(
        reverse("account:signup"),
        {
        "username": "testuser",
        "email": "dwfawdsadsadf",
        "age": "18",
        "password1": "dsadasfsadsadf",
        "password2": "testpass123",
        },
        )

        self.assertEqual(User.objects.all().count(), 0)
    
    def test_short_password(self):
        response = self.client.post(
        reverse("account:signup"),
        {
        "username": "testuser",
        "email": "dwfawdsadsadf",
        "age": 18,
        "password1": "aaa",
        "password2": "aaa",
        },
        )

        self.assertEqual(User.objects.all().count(), 0)