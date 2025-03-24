from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    temple_name = 'article_new.html'
    fields = ("title", "body")

    def form_valid(self, form):
        from.instance.author = self.requests.user
        return super().form_valid(form)
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user