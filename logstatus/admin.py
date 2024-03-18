from django.contrib import admin

from logstatus.models import LogMessage


@admin.register(LogMessage)
class LogMessageAdmin(admin.ModelAdmin):
    list_display = ('last_try', 'sending_status', 'id_mailing',)
