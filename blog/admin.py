from django.contrib import admin

# Register your models here.

from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
       list_display = [
        'name',
    ]
       
       
@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
       list_display = [
        'title',
        'author',
        'type',
        'content',
        
    ]
       
