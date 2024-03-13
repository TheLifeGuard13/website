from django.contrib import admin

from mailing.models import Period, Mailing


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('name', 'sending_time', 'period',)
    search_fields = ('name',)
