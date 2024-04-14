from django import forms
from django.forms import DateTimeInput

from mailing.models import Mailing
from website.forms import StyleFormMixin


class MailingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        exclude = (
            "owner",
            "status",
            "next_sending_time",
        )
        widgets = {
            "first_sending_time": DateTimeInput(attrs={"type": "datetime-local"}),
            "start_datetime": DateTimeInput(attrs={"type": "datetime-local"}),
            "end_datetime": DateTimeInput(attrs={"type": "datetime-local"}),
        }
        labels = {
            "sending_time": "Время рассылки",
            "start_datetime": "Время начала",
            "end_datetime": "Время конца",
        }
