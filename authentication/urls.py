# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import user_login_view, register_user, admin_login_view,forgot_password_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', user_login_view, name="login"),
    path('admin-login/', admin_login_view, name="admin_login"),
    path('forgot-password/', forgot_password_view, name="forgot_password"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout")
]
