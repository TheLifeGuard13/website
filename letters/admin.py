from django.contrib import admin

from letters.models import Letter


@admin.register(Letter)
class MailingAdmin(admin.ModelAdmin):
    list_display = (
        "letter_header",
        "letter_body",
    )
    search_fields = ("letter_header",)
