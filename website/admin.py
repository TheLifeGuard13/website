from django.contrib import admin

from website.models import Client, Period, Status, MailingSettings, Mailing, LogMessage


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'avatar', 'created_at', 'comment', )
    search_fields = ('email', 'name',)
    list_filter = ('created_at',)


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'sending_time', 'period',)
    search_fields = ('name',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('letter_header', 'letter_body', 'settings',)
    search_fields = ('letter_header', 'settings',)
    list_filter = ('settings',)


@admin.register(LogMessage)
class LogMessageAdmin(admin.ModelAdmin):
    list_display = ('client_email', 'letter_header', 'last_try', 'sending_status', 'server_answer', )
    search_fields = ('client_email', 'letter_header',)
    list_filter = ('sending_status', 'letter_header',)
