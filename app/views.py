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
from app.forms import *
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode
from django import forms


def validation_control(request, user_values=None):
    if not request.user.is_authenticated:
        if user_values['password'] != user_values['password2']:
            message = 'Şifreler eşleşmiyor!'
            return False, message
        if len(user_values['password']) < 6:
            message = 'Şifreniz çok kısa!'
            return False, message

        if 'yenikey' in user_values.keys():
            if user_values['yenikey']:  # Yenikeye özel val.
                message = 'Şifreler eşleşmiyor!'
                return False, message

    return True, ''


def complete_profile_view(request, uidb64, token):
    form = SignUpForm(request.POST or None)
    user_id = force_text(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=user_id)

    if user.is_profile_completed:
        message = 'Hesabınız zaten aktive edilmiş.'
        messages.warning(request, mark_safe(message))
        return redirect('user_login_view')

    if not request.user.is_authenticated:
        form.fields['password'].required = True
        form.fields['password2'].required = True

    if 'complete_profile' in request.POST:
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            password2 = form.cleaned_data.get("password2")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            sehir = form.cleaned_data.get("sehir")
            dogum_gunu = form.cleaned_data.get("dogum_gunu")
            cinsiyet = form.cleaned_data.get("cinsiyet")
            universite = form.cleaned_data.get("universite")
            sinif = form.cleaned_data.get("sinif")
            bolum = form.cleaned_data.get("bolum")
            company_name = form.cleaned_data.get("company_name")
            team_leader_checkbox = request.POST.get("team_leader_checkbox")

            if team_leader_checkbox:
                if Company.objects.filter(company_name__iexact=company_name):
                    message = 'Şirketinizde bir ekip lideri bulunuyor!'
                    messages.error(request, mark_safe(message))
                    return redirect('profile')
            else:
                team_leader_checkbox = False

            telefon = form.cleaned_data.get("telefon")
            linkedin_url = form.cleaned_data.get("linkedin_url")
            bio = form.cleaned_data.get("bio")

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
                'sinif': sinif,
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

                if account_activation_token.check_token(user, token):
                    user.email = user_values['email']
                    user.set_password(user_values['password'])
                    user.first_name = user_values['first_name']
                    user.last_name = user_values['last_name']
                    user.sehir = user_values['sehir']
                    user.dogum_gunu = user_values['dogum_gunu']
                    user.cinsiyet = user_values['cinsiyet']
                    user.universite = user_values['universite']
                    user.sinif = user_values['sinif']
                    user.bolum = user_values['bolum']
                    user.telefon = user_values['telefon']
                    user.linkedin_url = user_values['linkedin_url']
                    user.bio = user_values['bio']
                    user.company = company
                    user.is_teamleader = is_teamleader
                    user.is_profile_completed = True
                    user.is_active = True
                    user.save()

                if team_leader_checkbox:
                    return redirect('ekip')

                del request.session['user_values']
                message = 'Kaydınız başarıyla oluşturuldu.'
                messages.success(request, mark_safe(message))
                return redirect('user_login_view')
            else:
                messages.error(request, mark_safe(message))

    user_filler = user.__dict__
    form = SignUpForm(user_filler)
    context = {
        'form': form,
    }
    return render(request, 'profile.html', context=context)


@login_required(login_url="/login/")
def edit_profile(request):
    user = User.objects.get(id=request.user.id)
    firm = user.firm
    batches = Batch.objects.select_related().filter(firm=firm)

    form = SignUpForm(request.POST or None)
    if not request.user.is_authenticated:
        form.fields['password'].required = True
        form.fields['password2'].required = True

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
            sinif = form.cleaned_data.get("sinif")
            bolum = form.cleaned_data.get("bolum")
            company_name = form.cleaned_data.get("company_name")

            team_leader_checkbox = request.POST.get("team_leader_checkbox")

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
            user.sinif = sinif
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
        'batches': batches,
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
#                 return redirect('login')
#
#             messages.error(request, mark_safe(message))
#
#     return render(request, 'is_teamleader.html')


def ekip(request):
    user = User.objects.get(id=request.user.id)
    firm = user.firm
    batches = Batch.objects.select_related().filter(firm=firm)

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
            return redirect('user_login_view')

    # Save data of the user's when there is a change in form
    elif 'save_changes_on_company' in request.POST:
        if form.is_valid():
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
        'batches': batches,
    }
    return render(request, 'my_team.html', context=context)


@login_required(login_url="/login/")
def curriculum(request, batch_name):
    user = User.objects.get(id=request.user.id)
    firm = user.firm
    batches = Batch.objects.select_related().filter(firm=firm)

    batch = Batch.objects.get(batch_name=batch_name)
    batch_description = batch.batch_description
    modules = Module.objects.select_related().filter(batch_related=batch.id)
    content_list = Content.objects.filter(module_related__batch_related_id=batch.id)

    context = {
        'batches': batches,
        'batch_name': batch_name,
        'batch_description': batch_description,
        'modules': modules,
        'content_list': content_list,
    }

    return render(request, "curriculum.html", context=context)


@login_required(login_url="/login/")
def article_view(request, article_header, batch_name, module_name):
    user = User.objects.get(id=request.user.id)
    firm = user.firm
    batches = Batch.objects.select_related().filter(firm=firm)

    article = Article.objects.get(article_header__iexact=article_header)
    article_description = article.article_description
    date_created = article.date_created.strftime("%d/%m/%Y")
    image_900 = article.image_900
    text = article.text

    context = {
        "article_header": article_header,
        "article_description": article_description,
        "date_created": date_created,
        "image_900": image_900,
        "text": text,
        "batches": batches,
    }

    return render(request, "article.html", context=context)


@login_required(login_url="/login/")
def video_view(request, video_header, batch_name, module_name):
    user = User.objects.get(id=request.user.id)
    firm = user.firm
    batches = Batch.objects.select_related().filter(firm=firm)

    video_instance = Video.objects.get(video_header__iexact=video_header)
    date_created = video_instance.date_created.strftime("%d/%m/%Y")
    video_embedded = video_instance.video
    video_description = video_instance.video_description

    context = {
        "video_header": video_header,
        "video_description": video_description,
        "video_embedded": video_embedded,
        "date_created": date_created,
        "batches": batches,
    }

    return render(request, "video.html", context=context)


@login_required(login_url="/login/")
def anket_view(request, survey_header, batch_name, module_name):
    user = User.objects.get(id=request.user.id)
    firm = user.firm
    batches = Batch.objects.select_related().filter(firm=firm)

    survey = Survey.objects.get(survey_header__iexact=survey_header)
    date_created = survey.date_created.strftime("%d/%m/%Y")
    survey_description = survey.survey_description

    text_question_form = TextQuestionForm(request.POST or None)
    option_question_form = OptionQuestionForm(request.POST or None)
    choice_question_form = ChoiceQuestionForm(request.POST or None)

    form = forms.Form()

    text_questions = survey.text_question.all()
    option_questions = survey.option_question.all()
    choice_questions = survey.choice_question.all()
    my_questions = {}

    # Sorulara type ve sıra ataması yapıyoruz.
    for ques in text_questions:
        ques.type = 1
        my_questions[ques] = ques.q_order
    for ques in option_questions:
        ques.type = 2
        my_questions[ques] = ques.q_order
    for ques in choice_questions:
        ques.type = 3
        my_questions[ques] = ques.q_order

    my_questions = list({k: v for k, v in sorted(my_questions.items(), key=lambda item: item[1])}.keys())

    for my_question in my_questions:
        if my_question.type == 1:
            form.fields["text_question_" + str(my_question.id)] = text_question_form.fields['text_question']
            form.fields["text_question_" + str(my_question.id)].label = my_question.actual_question

        elif my_question.type == 2:
            form.fields["option_question_" + str(my_question.id)] = option_question_form.fields['option_question']
            form["option_question_" + str(my_question.id)].label = my_question.actual_question
            choices = []
            choice_objs = OptionChoice.objects.select_related().filter(actual_question=my_question)
            for obj in choice_objs:
                choices.append((obj.id, obj.choice))
            form["option_question_" + str(my_question.id)].choices = choices

        elif my_question.type == 3:
            form.fields["choice_question_" + str(my_question.id)] = choice_question_form.fields['choice_question']
            form["choice_question_" + str(my_question.id)].label = my_question.actual_question
            choices = []
            choice_objs = MultipleChoice.objects.select_related().filter(actual_question=my_question)
            for obj in choice_objs:
                choices.append((obj.id, obj.choice))
            form["choice_question_" + str(my_question.id)].choices = choices

    if 'submit_survey' in request.POST:
        query_dict = request.POST
        my_dict = dict(query_dict.items())
        del my_dict['csrfmiddlewaretoken']
        del my_dict['submit_survey']
        question_list = []
        for key in my_dict.keys():
            question_list.append(key)

        answer_list = []
        for value in my_dict.values():
            answer_list.append(value)

        survey_answer, is_created = SurveyAnswer.objects.get_or_create(
            defaults={'survey_participant': user},
            survey=survey,
        )

        for question in question_list:
            if 'text_question' in question:
                q_id = question.replace('text_question_', '')
                text_answer, is_created = SurveyAnswerFromQuestionText.objects.get_or_create(
                    defaults={'survey_answer': survey_answer},
                    question=TextQuestion.objects.get(pk=q_id),
                )
                text_answer.answer = my_dict[str(question)]
                text_answer.save()

            if 'option_question' in question:
                q_id = question.replace('option_question_', '')
                option_answer, is_created = SurveyAnswerFromQuestionOption.objects.get_or_create(
                    defaults={'survey_answer': survey_answer},
                    question=OptionQuestion.objects.get(pk=q_id),
                )
                option_answer.answer = OptionChoice.objects.get(pk=my_dict[question])
                option_answer.save()

            if 'choice_question' in question:
                q_id = question.replace('choice_question_', '')
                choice_answer, is_created = SurveyAnswerFromQuestionChoice.objects.get_or_create(
                    defaults={'survey_answer': survey_answer},
                    question=MultipleQuestion.objects.get(pk=q_id),
                )
                choice_answer.answer = MultipleChoice.objects.get(pk=my_dict[question])
                choice_answer.save()

        msg = "Cevaplarınız başarıyla iletildi"
        messages.success(request, mark_safe(msg))

        context = {
            'batches': batches
        }
        return redirect('curriculum', context=context)

    context = {
        "survey_header": survey_header,
        "survey_description": survey_description,
        "date_created": date_created,
        "my_questions": my_questions,
        "form": form,
    }

    return render(request, "anket.html", context=context)
