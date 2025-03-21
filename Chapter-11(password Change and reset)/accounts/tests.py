from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class SignuupPageTest(TestCase):
    def test_url_exists_at_correct_location_signupview(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
    def test_signup_view_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,"registration/signup.html")
    def test_signup_form(self):
        response = self.client.post(reverse("signup"),
                                    {
                                        "username" : "x",
                                        "email" : "x@gmail.com"
                                        "password1" : "x"
                                        "password2" : "x"
                                    })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().object.all().count(),1)