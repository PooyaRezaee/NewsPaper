from django.shortcuts import render
from django.views.generic import ListView,DetailView,DeleteView,UpdateView
from .models import Article
from django.urls import reverse_lazy

__all__ = [
    'ArticleListView',
    'ArticleDetailView',
    'ArticleUpdateView',
    'ArticleDeleteView',
]

class ArticleListView(ListView):
    model = Article
    template_name = "article/article_list.html"
    context_object_name = 'articles'

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article/article_detail.html"
    context_object_name = 'article'

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ("title","body")
    template_name = "article/article_edit.html"

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "article/article_delete.html"
    success_url = reverse_lazy("article:article_list")
