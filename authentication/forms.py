from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from app.models import *


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "E-posta",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Şifre",
                "class": "form-control"
            }
        ))


class AdminLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "E-posta",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Şifre",
                "class": "form-control"
            }
        ))


class ForgetForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "E-posta",
                "class": "form-control"
            }
        ))


class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Şifre",
                "class": "form-control"
            }
        ))
    password_check = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Şifre Tekrar",
                "class": "form-control"
            }
        ))


class SignUpForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "E-posta",
                "class": "form-control form-control-alternative"
            }
        ),
        required=True
    )
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Parola",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Parolayı Onayla",
                "class": "form-control"
            }
        ))
    first_name = forms.CharField(
        disabled=False,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-alternative"
            }
        )
    )
    last_name = forms.CharField(
        disabled=False,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-alternative"
            }
        )
    )
    sehir = forms.ChoiceField(
        required=True,
        disabled=False,
        choices=Cities,
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )
    dogum_gunu = forms.DateField(
        required=True,
        disabled=False,
        widget=forms.DateInput(
            attrs={
                "date-date-format": "dd/mm/yyyy",
                "format": "dd-mm-yyyy",
                "class": "form-control datepicker",
            }
        ),
    )
    cinsiyet = forms.ChoiceField(
        required=True,
        disabled=False,
        choices=Cinsiyetler,
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )
    universite = forms.ChoiceField(
        required=True,
        disabled=False,
        choices=universiteler,
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        ),
    )
    # User._meta.get_field('universite').help_text
    sinif = forms.ChoiceField(
        required=True,
        disabled=False,
        choices=Siniflar,
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        ),
    )
    bolum = forms.ChoiceField(
        required=True,
        disabled=False,
        choices=bolumler,
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        ),
    )
    company_name = forms.ChoiceField(
        disabled=False,
        choices=Girisimler,
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        ),
    )
    # team_leader_checkbox = forms.BooleanField(
    #     label="Ekip Lideriyim",
    #     required=False,
    #     disabled=False,
    #     widget=forms.CheckboxInput(
    #
    #         attrs={
    #             "data-toggle": "tooltip",
    #             "title": "Ekipte yalnızca tek lider olabileceğini unutma!",
    #             "class": "custom-control-input",
    #             "label.class": "custom-control-label"
    #         }
    #     ),
    # )
    telefon = forms.CharField(
        max_length=User._meta.get_field('telefon').max_length,
        disabled=False,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "05*********",
                "class": "form-control form-control-alternative"
            }
        )
    )
    linkedin_url = forms.URLField(
        required=False,
        widget=forms.URLInput(
            attrs={
                "placeholder": "URL şeklinde giriniz.",
                "class": "form-control form-control-alternative"
            }
        )
    )
    bio = forms.CharField(
        max_length=User._meta.get_field('bio').max_length,
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Kısaca kendinden bahset",
                "rows": "5",
                "class": "form-control form-control-alternative"
            }
        )
    )

    # class Meta:
    #     model = User
    #     fields = ('email', 'password', 'first_name', 'telefon', 'sehir', 'universite', 'bolum', 'sınıf', 'linkedin_url', 'bio', 'cinsiyet', 'dogum_gunu')


class CompanyForm(forms.Form):
    company_name = forms.ChoiceField(
        disabled=False,
        choices=Girisimler,
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        ),
    )
    team_size = forms.IntegerField(
        required=True,
        disabled=False,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control form-control-alternative",
                "placeholder": "Sayı ile giriniz.",
                "id": "input-kisi_sayisi"
            }
        ),
    )
    is_tech_exist = forms.ChoiceField(
        required=True,
        disabled=False,
        choices=Is_Tech_Exist,
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        ),
    )
    bootcamp_name = forms.ChoiceField(
        required=True,
        disabled=False,
        choices=universiteler,
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        ),
    )
    enterprise_category = forms.ChoiceField(
        required=True,
        disabled=False,
        choices=Girisim_Kategorileri,
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        ),
    )
    enterprise_summary = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Kısaca girişiminizden bahsedin.",
                "rows": "5",
                "max_length": "450",
                "id": "my-textarea",
                "class": "form-control form-control-alternative"
            }
        )
    )


class CompanyDisabledFields(CompanyForm):
    company_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'readonly': 'readonly',
                "class": "form-control"
            }
        ),
    )
    team_size = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'readonly': 'readonly',
                "class": "form-control form-control-alternative",
                "placeholder": "Sayı ile giriniz.",
                "id": "input-kisi_sayisi"
            }
        ),
    )
    is_tech_exist = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'readonly': 'readonly',
                "class": "form-control"
            }
        ),
    )
    bootcamp_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'readonly': 'readonly',
                "class": "form-control"
            }
        ),
    )
    enterprise_category = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'readonly': 'readonly',
                "class": "form-control"
            }
        ),
    )
    enterprise_summary = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'readonly': 'readonly',
                "placeholder": "Kısaca girişiminizden bahsedin.",
                "rows": "5",
                "max_length": "450",
                "id": "my-textarea",
                "class": "form-control form-control-alternative"
            }
        )
    )
