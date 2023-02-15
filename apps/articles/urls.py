from django.urls import path
from .views import *

app_name = 'article'

urlpatterns = [
    path("", ArticleListView.as_view(), name="article_list"),
]
