
from django.test import SimpleTestCase
from django.urls import reverse


class HomepageTest(SimpleTestCase):
    def  test_url_exist_at_correct_locations(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response, "home.html")
    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response, "<h1>Homepage</h1>")






class AboutpageTest(SimpleTestCase):
    def  test_url_exist_at_correct_locations(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response, "about.html")
    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response, "<h1>About page</h1>")
