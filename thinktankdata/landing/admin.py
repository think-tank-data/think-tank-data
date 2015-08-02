from django.contrib import admin
from .models import *

# Register your models here.

class SitewideAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','headline', 'coverphoto']
    list_display_links = ['id',]
    readonly_fields=('id',)
    search_fields = ['name',]
admin.site.register(Sitewide, SitewideAdmin)

class SubNotesAdmin(admin.ModelAdmin):
    list_display = ['id', 'subheadline','subtext', 'priority']
    list_display_links = ['id',]
    readonly_fields=('id',)
    search_fields = ['subheadlines','subtext']
admin.site.register(SubNotes, SubNotesAdmin)

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug','name', 'priority']
    list_display_links = ['id',]
    readonly_fields=('id',)
    search_fields = ['slug','name']
admin.site.register(Categories, CategoriesAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug','name', 'priority']
    list_display_links = ['id',]
    readonly_fields=('id',)
    search_fields = ['slug','name']
admin.site.register(Tag, TagAdmin)

class ThinktankAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug','name', 'priority']
    list_display_links = ['id',]
    readonly_fields=('id',)
    search_fields = ['slug','name']
admin.site.register(Thinktank, ThinktankAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug','pub_date', 'headline', 'body', 'source', 'author']
    list_display_links = ['id',]
    readonly_fields=('id',)
    search_fields = ['slug','headline', 'body']
admin.site.register(Article, ArticleAdmin)

class DatasetAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'name', 'priority', 'source', 'article']
    list_display_links = ['id',]
    readonly_fields=('id',)
    search_fields = ['slug','slug', 'name']
admin.site.register(Dataset, DatasetAdmin)
