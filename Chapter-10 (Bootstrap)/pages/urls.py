from django.contrib import admin
from django.urls import path, include

from .views import HomePageView

urlpatters = {
    path("", HomePageView.as_view(), name="home"),
}