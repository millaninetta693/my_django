from django.contrib import admin
from .models import Reference


@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link', 'author', 'created', 'updated', 'slug')
    list_filter = ('created', 'author')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    raw_id_fields = ('author',)
    ordering = ('created',)
# Register your models here.
