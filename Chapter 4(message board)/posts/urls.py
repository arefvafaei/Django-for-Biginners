from django.urls import path
from .views import HomePageView

urlpattern = [
    path("", HomePageView.as_view(), name="home"),
]
