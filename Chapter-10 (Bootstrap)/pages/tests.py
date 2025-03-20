from django.test import SimpleTestCase
from django.urls import reverse

class HomePagesTest(SimpleTestCase):
    def test_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)