# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import *

# Register your models here.


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'company', 'date_joined', 'firm', 'is_firm_manager')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(firm=request.user.firm)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):

    list_display = ['id', 'company_name', 'team_size', 'is_tech_exist', 'girisim_kategorisi', 'bootcamp_name', 'enterprise_summary']
    # list_editable = ['code', 'valid_from', 'valid_to', 'value', ]
    search_fields = ['company_name', ]
    list_filter = ['team_size', 'is_tech_exist', ]


@admin.register(Firm)
class FirmAdmin(admin.ModelAdmin):

    list_display = ['id', 'firm_name', 'firm_domain']
    # list_editable = ['code', 'valid_from', 'valid_to', 'value', ]
    search_fields = ['firm_name', ]
    # list_filter = ['team_size', 'is_tech_exist', ]


# @admin.register(Survey)
# class SurveyAdmin(admin.ModelAdmin):
#
#     list_display = ['id', 'survey_header', 'survey_description', 'date_created',]
#     # list_editable = ['code', 'valid_from', 'valid_to', 'value', ]
#     # search_fields = ['firm_name', ]
#     # list_filter = ['team_size', 'is_tech_exist', ]
#
#     class Meta:
#         model = Survey

class MultipleChoiceAdmin(admin.TabularInline):

    model = MultipleChoice


@admin.register(MultipleQuestion)
class MultipleQuestionAdmin(admin.ModelAdmin):

    inlines = [
        MultipleChoiceAdmin,
    ]



class OptionChoiceAdmin(admin.TabularInline):

    model = OptionChoice


@admin.register(OptionQuestion)
class OptionQuestionAdmin(admin.ModelAdmin):

    inlines = [
        OptionChoiceAdmin,
    ]


class TextAnswerAdmin(admin.TabularInline):
    readonly_fields = ('question', 'answer')
    model = SurveyAnswerFromQuestionText


class OptionAnswerAdmin(admin.TabularInline):
    readonly_fields = ('question', 'answer')
    model = SurveyAnswerFromQuestionOption


class ChoiceAnswerAdmin(admin.TabularInline):
    readonly_fields = ('question', 'answer')
    model = SurveyAnswerFromQuestionChoice


@admin.register(SurveyAnswer)
class SurveyAnswerAdmin(admin.ModelAdmin):
    readonly_fields = ('survey', 'survey_participant')
    inlines = [
        TextAnswerAdmin,
        OptionAnswerAdmin,
        ChoiceAnswerAdmin,
    ]

    list_display = ['survey_participant', 'survey']


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    readonly_fields = ('firm',)

    def save_model(self, request, obj, form, change):
        obj.firm = request.user.firm
        super().save_model(request, obj, form, change)


admin.site.register(Article)
admin.site.register(Video)
admin.site.register(Survey)
admin.site.register(Module)
admin.site.register(TextQuestion)
admin.site.register(Content)
