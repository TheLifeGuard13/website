# from django.contrib import admin
#
# from website.models import Period, Status, MailingSettings, Mailing, LogMessage
#
#
# @admin.register(Period)
# class PeriodAdmin(admin.ModelAdmin):
#     list_display = ('name', )
#
#
# @admin.register(Status)
# class StatusAdmin(admin.ModelAdmin):
#     list_display = ('name', )
#
#
# @admin.register(MailingSettings)
# class MailingSettingsAdmin(admin.ModelAdmin):
#     list_display = ('name', 'sending_time', 'period',)
#     search_fields = ('name',)
#
#

#
#
# @admin.register(LogMessage)
# class LogMessageAdmin(admin.ModelAdmin):
#     list_display = ('client_email', 'letter_header', 'last_try', 'sending_status', 'server_answer', )
#     search_fields = ('client_email', 'letter_header',)
#     list_filter = ('sending_status', 'letter_header',)
