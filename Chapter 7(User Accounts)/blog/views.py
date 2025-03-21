from django.urls import reverse_lazy
from django.views.generic import ListView, DateDetailView, CreateView, UpdateView, DeleteView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DateDetailView):
    model = Post
    template_name = "post_detail.html"

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title","author","body"]

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title" "body"]

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete"
    success_url = reverse_lazy("home")
