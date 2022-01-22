from django.contrib import admin
from .models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('author','content','keywords','title')
    

admin.site.register(Article, ArticleAdmin)