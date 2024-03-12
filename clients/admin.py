from django.contrib import admin

from clients.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'avatar', 'created_at', 'comment', )
    search_fields = ('email', 'name',)
    list_filter = ('created_at',)
