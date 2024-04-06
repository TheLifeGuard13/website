from django import forms

from letters.models import Letter
from website.forms import StyleFormMixin


class LetterForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Letter
        exclude = ('owner', )
