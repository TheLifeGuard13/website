from django.contrib import admin

from mailing.models import Mailing


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('is_active', 'first_sending_time', 'period',
                    'name', 'start_datetime', 'end_datetime', 'created_at', 'status',)
    search_fields = ('name',)
    filter_fields = ('is_active', 'period', 'status',)
