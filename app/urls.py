# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('şirket/', views.ekip, name='ekip'),
    # path('plan/', views.is_teamleader, name='is_teamleader')
    path('kullanıcılar/', views.Bulk_Add_Users, name='Bulk_Add_Users'),
    path('profil/', views.edit_profile, name='profile'),
    path('curriculum/<batch_name>/', views.curriculum, name='curriculum'),
    path('curriculum/<batch_name>/<module_name>/yazi/<article_header>', views.article_view, name='article_view'),
    path('curriculum/<batch_name>/<module_name>/video/<video_header>', views.video_view, name='video_view'),
    path('curriculum/<batch_name>/<module_name>/anket/<survey_header>', views.anket_view, name='anket_view'),
    path('activate/<uidb64>/<token>', views.complete_profile_view, name='complete_profile_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

