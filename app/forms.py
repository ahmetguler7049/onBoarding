from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from app.models import *


class TextQuestionForm(forms.Form):
    text_question = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": "4",
                "placeholder": "Cevabınız...",
                "aria-required": "False",
            }
        )
    )


class OptionQuestionForm(forms.Form):
    option_question = forms.ChoiceField(
        required=False,
        disabled=False,
        choices=[],
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "aria-required": "False",
            }
        ),
    )


class ChoiceQuestionForm(forms.Form):
    choice_question = forms.ChoiceField(
        required=False,
        disabled=False,
        choices=[],
        widget=forms.RadioSelect(
            attrs={
                "class": "custom-control custom-radio mb-1",
                "aria-required": "False",
            }
        ),
    )
