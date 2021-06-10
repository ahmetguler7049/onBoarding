from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from authentication.views import *
from django.contrib import messages
from django import template
from django.utils.safestring import mark_safe
from .models import *
from django.db.models import Q
from authentication.forms import SignUpForm, CompanyForm, CompanyDisabledFields


# from django.contrib.auth.models import User


@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")


def validation_control(request, user_values=None):
    if not request.user.is_authenticated:
        if user_values['password'] != user_values['password2']:
            message = 'Şifreler eşleşmiyor!'
            return False, message

        if 'yenikey' in user_values.keys():
            if user_values['yenikey']:  # Yenikeye özel val.
                message = 'Şifreler eşleşmiyor!'
                return False, message

    return True, ''


def profile(request):
    form = SignUpForm(request.POST or None)
    if not request.user.is_authenticated:
        form.fields['password'].required = True
        form.fields['password2'].required = True

    if 'complete_profile' in request.POST:
        print('1' * 40)
        if form.is_valid():
            print('2' * 40)
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            password2 = form.cleaned_data.get("password2")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            sehir = form.cleaned_data.get("sehir")
            dogum_gunu = form.cleaned_data.get("dogum_gunu")
            cinsiyet = form.cleaned_data.get("cinsiyet")
            universite = form.cleaned_data.get("universite")
            sınıf = form.cleaned_data.get("sınıf")
            bolum = form.cleaned_data.get("bolum")
            company_name = form.cleaned_data.get("company_name")

            team_leader_checkbox = request.POST.get("team_leader_checkbox")
            user = User.objects.get(id=request.user.id)

            if team_leader_checkbox:
                if User.objects.filter(is_teamleader=True, company__id=user.company.id):
                    message = 'Şirketinizde bir ekip lideri bulunuyor!'
                    messages.error(request, mark_safe(message))
                    return redirect('profile')
            else:
                team_leader_checkbox = False

            telefon = form.cleaned_data.get("telefon")
            linkedin_url = form.cleaned_data.get("linkedin_url")
            bio = form.cleaned_data.get("bio")

            # dogum_gunu_obj = timezone.datetime.strptime(dogum_gunu, '%Y-%m-%d')
            # dogum_gunu_timestamp = dogum_gunu_obj.timestamp()
            user_values = {
                'email': email,
                'password': password,
                'password2': password2,
                'first_name': first_name,
                'last_name': last_name,
                'sehir': sehir,
                'dogum_gunu': str(dogum_gunu),
                'cinsiyet': cinsiyet,
                'universite': universite,
                'sınıf': sınıf,
                'bolum': bolum,
                'company_name': company_name,
                'team_leader_checkbox': team_leader_checkbox,
                'telefon': telefon,
                'linkedin_url': linkedin_url,
                'bio': bio,
            }
            success, message = validation_control(request, user_values=user_values)
            if success:
                request.session['user_values'] = user_values
                company, created = Company.objects.get_or_create(
                    defaults={'company_name': company_name},
                    company_name__iexact=company_name
                )

                if team_leader_checkbox:
                    is_teamleader = True
                else:
                    is_teamleader = False

                User.objects.create_user(
                    email=user_values['email'],
                    password=user_values['password'],
                    first_name=user_values['first_name'],
                    last_name=user_values['last_name'],
                    sehir=user_values['sehir'],
                    dogum_gunu=user_values['dogum_gunu'],
                    cinsiyet=user_values['cinsiyet'],
                    universite=user_values['universite'],
                    sınıf=user_values['sınıf'],
                    bolum=user_values['bolum'],
                    telefon=user_values['telefon'],
                    linkedin_url=user_values['linkedin_url'],
                    bio=user_values['bio'],
                    company=company,
                    is_teamleader=is_teamleader,
                    is_profile_completed=True
                )

                if team_leader_checkbox:
                    return redirect('ekip')

                del request.session['user_values']
                message = 'Kaydınız başarıyla oluşturuldu.'
                messages.success(request, mark_safe(message))
                return redirect('home')
            else:
                messages.error(request, mark_safe(message))

    if 'save_changes_onprofile' in request.POST:
        # print(request.POST)
        # print(form.errors)
        if form.is_valid():
            # print(form.errors)
            email = form.cleaned_data.get("email")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            sehir = form.cleaned_data.get("sehir")
            dogum_gunu = form.cleaned_data.get("dogum_gunu")
            cinsiyet = form.cleaned_data.get("cinsiyet")
            universite = form.cleaned_data.get("universite")
            sınıf = form.cleaned_data.get("sınıf")
            bolum = form.cleaned_data.get("bolum")
            company_name = form.cleaned_data.get("company_name")

            team_leader_checkbox = request.POST.get("team_leader_checkbox")

            user = request.user
            if user.company:
                delete_company = user.company.company_name
            else:
                delete_company = None

            company, created = Company.objects.get_or_create(
                defaults={'company_name': company_name},
                company_name__iexact=company_name
            )

            if team_leader_checkbox:
                if user.is_teamleader:
                    team_leader_checkbox = True

                elif User.objects.filter(is_teamleader=True, company__id=user.company.id):
                    message = 'Şirketinizde bir ekip lideri bulunuyor!'
                    messages.error(request, mark_safe(message))
                    return redirect('profile')
                else:
                    team_leader_checkbox = True
            else:
                team_leader_checkbox = False

            telefon = form.cleaned_data.get("telefon")
            linkedin_url = form.cleaned_data.get("linkedin_url")
            bio = form.cleaned_data.get("bio")

            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.sehir = sehir
            user.dogum_gunu = dogum_gunu
            user.cinsiyet = cinsiyet
            user.universite = universite
            user.sınıf = sınıf
            user.bolum = bolum
            user.is_teamleader = team_leader_checkbox
            user.telefon = telefon
            user.linkedin_url = linkedin_url
            user.bio = bio
            user.company = company
            user.save()

            if company.company_name != delete_company and delete_company:
                user_companies = User.objects.filter(company__company_name=delete_company)
                if not len(user_companies):
                    Company.objects.get(company_name__iexact=delete_company).delete()

            return redirect('profile')

    # Save data of the user's when there is a change in form
    # Don't forget to add company_name key to user_filler dict since there is not any company_name data in User object.
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        user_filler = user.__dict__
        if user.company:
            user_filler['company_name'] = user.company.company_name
        form = SignUpForm(user_filler)

    context = {
        'form': form,
    }
    return render(request, 'profile.html', context=context)


# def is_teamleader(request):
#
#     if request.method == 'POST':
#         user_values = request.session['user_values']
#
#         user_values['yenikey'] = ''
#         success, message = validation_control(request, user_values)
#
#         if 'continue_ekip' in request.POST:
#             return redirect('ekip')
#
#         elif 'complete_profile' in request.POST:
#             if success:
#                 # request.session['user_values'] = user_values
#                 del request.session['user_values']
#
#                 user = User.objects.create_user(
#                     email=user_values['email'],
#                     password=user_values['password'],
#                     first_name=user_values['first_name'],
#                     sehir=user_values['sehir'],
#                     dogum_gunu=user_values['dogum_gunu'],
#                     cinsiyet=user_values['cinsiyet'],
#                     universite=user_values['universite'],
#                     sınıf=user_values['sınıf'],
#                     bolum=user_values['bolum'],
#                     telefon=user_values['telefon'],
#                     linkedin_url=user_values['linkedin_url'],
#                     bio=user_values['bio'],
#                 )
#
#                 message = 'Kaydınız başarıyla oluşturuldu.'
#                 messages.success(request, mark_safe(message))
#                 return redirect('home')
#
#             messages.error(request, mark_safe(message))
#
#     return render(request, 'is_teamleader.html')


def ekip(request):
    form = CompanyForm(request.POST or None)

    if 'complete_company' in request.POST:
        if form.is_valid():
            company_name = form.cleaned_data.get("company_name")
            team_size = form.cleaned_data.get("team_size")
            is_tech_exist = form.cleaned_data.get("is_tech_exist")
            bootcamp_name = form.cleaned_data.get("bootcamp_name")
            enterprise_category = form.cleaned_data.get("enterprise_category")
            enterprise_summary = form.cleaned_data.get("enterprise_summary")

            company = Company.objects.get(company_name__iexact=company_name)
            company.team_size = team_size
            company.bootcamp_name = bootcamp_name
            company.is_tech_exist = is_tech_exist
            company.enterprise_summary = enterprise_summary
            company.girisim_kategorisi = enterprise_category
            company.save()

            del request.session['user_values']
            message = 'Kaydınız başarıyla oluşturuldu.'
            messages.success(request, mark_safe(message))
            return redirect('home')

    # Save data of the user's when there is a change in form
    elif 'save_changes_on_company' in request.POST:
        if form.is_valid():
            user = User.objects.get(id=request.user.id)
            if user.is_teamleader:
                company_name = form.cleaned_data.get("company_name")
                team_size = form.cleaned_data.get("team_size")
                is_tech_exist = form.cleaned_data.get("is_tech_exist")
                bootcamp_name = form.cleaned_data.get("bootcamp_name")
                enterprise_category = form.cleaned_data.get("enterprise_category")
                enterprise_summary = form.cleaned_data.get("enterprise_summary")

                company = Company.objects.get(company_name__iexact=company_name)
                company.team_size = team_size
                company.bootcamp_name = bootcamp_name
                company.is_tech_exist = is_tech_exist
                company.enterprise_summary = enterprise_summary
                company.girisim_kategorisi = enterprise_category
                company.save()

                return redirect('ekip')

    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        if user.company:
            company_filler = Company.objects.get(id=user.company_id)
            company_filler = company_filler.__dict__
            company_filler['enterprise_category'] = dict.pop(company_filler, 'girisim_kategorisi')
            if user.is_teamleader:
                form = CompanyForm(company_filler)
            else:
                form = CompanyDisabledFields(company_filler)

    context = {
        'form': form,
    }
    return render(request, 'my_team.html', context=context)
