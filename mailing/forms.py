from django import forms

from mailing.models import Mailing
from website.forms import StyleFormMixin


class LetterForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        exclude = ('owner', )
