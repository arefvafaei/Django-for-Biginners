from django.shortcuts import render

from django.views.generic import ListView,DateDetailView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DateDetailView):
    model = Post
    template_name = "post_detail.html"