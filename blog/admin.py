from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('owner', 'header', 'description', 'preview', 'views_count', 'published_at', )
    search_fields = ('header', 'description',)
    list_filter = ('owner', 'published_at',)
