from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Poste)
class PosteAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'created_at')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('autor', 'added_at', 'content', 'show')
    list_filter = ('show', 'added_at', 'autor')
    search_fields = ('autor',)