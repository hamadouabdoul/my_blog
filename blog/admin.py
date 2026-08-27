from django.contrib import admin
from .models import *

# Register your models here.

@admin.site.register(Poste)
class PosteAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'created_at')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title',)