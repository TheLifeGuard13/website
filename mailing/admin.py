from django.contrib import admin

from mailing.models import Mailing


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('name', 'sending_time', 'period', 'is_active',)
    search_fields = ('name',)
