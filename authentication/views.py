# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
from django.core.exceptions import *

from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm, ForgetForm, ResetPasswordForm, AdminLoginForm

from app.models import *

from django.contrib import messages
from django.utils.safestring import mark_safe

import json
import urllib.request
import urllib.parse
from django.conf import settings


def recaptcha_kontrol(request):
    recaptcha_response = request.POST.get('g-recaptcha-response')
    url = 'https://www.google.com/recaptcha/api/siteverify'
    values = {
        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
    }
    data = urllib.parse.urlencode(values).encode()
    req = urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(req)
    result = json.loads(response.read().decode())
    return result


def user_login_view(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form,
    }

    if request.method == "POST":

        if form.is_valid():
            result = recaptcha_kontrol(request)

            if result['success']:
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')

                try:
                    findUser = User._default_manager.get(email__iexact=email)
                    if findUser is not None:
                        if findUser.check_password(password):
                            user_login_check = authenticate(username=findUser, password=password)
                            login(request, user_login_check)
                            return redirect("/")
                        else:
                            messages.error(request, mark_safe('Geçersiz Şifre!'))
                except User.DoesNotExist:
                    messages.error(request, mark_safe('E-posta adresi bulunamadı!'))
            else:
                messages.error(request, mark_safe('Geçersiz reCAPTCHA. Lütfen tekrar deneyin.'))
        else:
            messages.error(request, mark_safe('Tüm alanları eksiksiz bir şekilde doldurduğunuzdan emin olun!'))

    return render(request, "accounts/login.html", context=context)


# TODO: Admin Login View'a göre formu özelleştir.

def admin_login_view(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form,
    }

    if request.method == "POST":

        if form.is_valid():
            result = recaptcha_kontrol(request)

            if result['success']:
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')

                if not form.cleaned_data.get('remember_me'):
                    request.session.set_expiry(0)

                try:
                    findUser = User._default_manager.get(email__iexact=email)
                    if findUser is not None:
                        if findUser.check_password(password):
                            user_login_check = authenticate(username=findUser, password=password)
                            login(request, user_login_check)
                            return redirect("/")
                        else:
                            messages.error(request, mark_safe('Geçersiz Şifre!'))
                except User.DoesNotExist:
                    messages.error(request, mark_safe('E-posta adresi bulunamadı!'))
            else:
                messages.error(request, mark_safe('Geçersiz reCAPTCHA. Lütfen tekrar deneyin.'))
        else:
            messages.error(request, mark_safe('Tüm alanları eksiksiz bir şekilde doldurduğunuzdan emin olun!'))

    return render(request, "accounts/admin_login.html", context=context)


def forget_password_view(request):
    form = ForgetForm(request.POST or None)
    msg = None

    if request.method == "POST":

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/forget_password.html", {"form": form, "msg": msg})


# def reset_password_view(request):
#
#     form = ResetPasswordForm(request.POST or None)
#     msg = None
#
#     if request.method == "POST":
#
#         if form.is_valid():
#             email = request.POST['email']
#             password = request.POST['password']
#             username = get_user(email)
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect("/")
#             else:
#                 msg = 'Invalid credentials'
#         else:
#             msg = 'Error validating the form'
#
#     return render(request, "accounts/reset-password.html", {"form": form, "msg" : msg})


# def register_user(request):
#     msg = None
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             msg = 'User created - please <a href="/login">login</a>.'
#             # return redirect("/login/")
#
#         else:
#             msg = 'Form is not valid'
#     else:
#         form = SignUpForm()
#
#     return render(request, "accounts/register.html", {"form": form, "msg": msg})
