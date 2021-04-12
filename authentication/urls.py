
from django.urls import path
from .views import user_login_view, admin_login_view, forget_password_view, register_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', user_login_view, name="login"),
    path('admin-login/', admin_login_view, name="admin_login"),
    path('forget-password/', forget_password_view, name="forget_password"),
    # path('reset-password/', reset_password_view, name="reset_password"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout")
]
