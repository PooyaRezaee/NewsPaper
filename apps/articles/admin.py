from django.contrib import admin
from .models import Article,Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','count_article')
    
    def count_article(self,obj):
        count = obj.article.count()
        return str(count)
    count_article.short_description = 'count'

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author','created')
    list_filter = ('created','modified')

