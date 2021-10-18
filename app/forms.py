from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from app.models import *


# class TextQuestionForm(forms.ModelForm):
#     class Meta:
#         model = TextQuestion
#         fields = ['text_answer']
#         labels = {}
#         widgets = {
#             'text_answer': forms.TextInput(
#                 attrs={
#                     "class": "form-control",
#                     "rows": "4",
#                     "placeholder": "Cevabınız..."
#                 }
#             )
#         }


class TextQuestionForm(forms.Form):
    text_question = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": "4",
                "placeholder": "Cevabınız..."
            }
        )
    )


class OptionQuestionForm(forms.Form):
    option_question = forms.ChoiceField(
        required=True,
        disabled=False,
        choices=[],
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        ),
    )


class ChoiceQuestionForm(forms.Form):
    choice_question = forms.ChoiceField(
        required=True,
        disabled=False,
        choices=[],
        widget=forms.RadioSelect(
            attrs={
                "class": "custom-control custom-radio mb-1"
            }
        ),
    )
