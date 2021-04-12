from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from authentication.views import *
from django import template
from django.contrib import messages
from django.utils.safestring import mark_safe
from .models import user
from django.contrib.auth.models import User


@login_required(login_url="/login/")
def index(request):
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


def profile(request):
    form = SignUpForm(request.POST or None)
    context = {
        'form': form,
    }

    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        if 'complete_profile' == "POST":
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            confirm = form.cleaned_data.get("password2")

            if password and confirm and password != confirm:
                mesaj = 'Parolalar eşleşmiyor!'
                if 'password' in form._errors:
                    form._errors["password"].append(mesaj)
                else:
                    form._errors["password"] = [mesaj]
                form._errors["confirm"] = [mesaj]

                messages.error(request, mark_safe(mesaj))

            if form.is_valid():
                user.user.first_activation = True
                user.user.save()
                user.is_active = True
                user.save()
                messages.success(request, mark_safe('Kayıt işlemi başarılı'))
                # return redirect("/login/")

            else:
                messages.error(request, mark_safe('Geçersiz form bilgisi!'))

        return render(request, 'profile.html', context=context)


def ekip(request):
    if request.user.is_authenticated:
        return render(request, 'my_team.html')
    else:
        return render(request, 'my_team.html')

def is_teamleader(request):
    return render(request, 'is_teamleader.html')
