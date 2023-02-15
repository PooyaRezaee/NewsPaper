from django.db import models
from django.urls import reverse
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=32)

class Article(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True,related_name='article')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,null=True,related_name='article')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("article:article_detail", kwargs={"pk": self.pk})
