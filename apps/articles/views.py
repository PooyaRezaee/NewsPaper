from django.shortcuts import render
from django.views.generic import ListView,DetailView,DeleteView,UpdateView,CreateView,FormView

from .models import Article,Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm

__all__ = [
    'ArticleListView',
    'ArticleDetailView',
    'ArticleUpdateView',
    'ArticleDeleteView',
    'ArticleCreateView'
]

class ArticleListView(ListView):
    model = Article
    template_name = "article/article_list.html"
    context_object_name = 'articles'

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article/article_detail.html"
    context_object_name = 'article'

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            Comment.objects.create(comment=cd['comment'],author=request.user,article=self.get_object())

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["form"] = CommentForm()
        context["comments"] = Comment.objects.filter(article=context['article'])
        return context


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ("title","body")
    template_name = "article/article_edit.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "article/article_delete.html"
    success_url = reverse_lazy("article:article_list")

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = "article/article_new.html"
    fields = (
    "title",
    "body",
    "category",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)