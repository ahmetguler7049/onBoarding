# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from app import views


urlpatterns = [
    path('', views.index, name='home'),
    path('profil/', views.profile, name='profile'),
    path('şirket/', views.ekip, name='ekip'),
    # path('plan/', views.is_teamleader, name='is_teamleader')
]
