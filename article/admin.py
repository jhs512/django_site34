from django.contrib import admin

# Register your models here.
from article.models import Article

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['id', 'create_date', 'author', 'title']

admin.site.register(Article, ArticleAdmin)