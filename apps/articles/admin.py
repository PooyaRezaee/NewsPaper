from django.contrib import admin
from .models import Article,Category,Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','count_article')
    
    def count_article(self,obj):
        count = obj.article.count()
        return str(count)
    count_article.short_description = 'count'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article','author','created')
    list_filter = ('created',)


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author','created')
    list_filter = ('created','modified')

    inlines = [
        CommentInline,
    ]


