from django.urls import path
from .views import user_login_view, admin_login_view, forget_password_view, index, reset_password_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name="home"),
    path('login/', user_login_view, name="user_login_view"),
    path('admin-login/', admin_login_view, name="admin_login_view"),
    path('sifre-yenile/<uidb64>/<token>', reset_password_view, name="reset_password"),
    path('sifremi-unuttum/', forget_password_view, name="forget_password"),
    # path('register/', register_user, name="register"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
