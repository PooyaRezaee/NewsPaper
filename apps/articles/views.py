from django.shortcuts import render
from django.views.generic import ListView
from .models import Article

__all__ = [
    'ArticleListView',
]

class ArticleListView(ListView):
    model = Article
    template_name = "article/article_list.html"
    context_object_name = 'articles'