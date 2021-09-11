
from django.urls import path
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

from .views import *


app_name = 'accounts'
urlpatterns = [
    path("profile/", profile, name='profile'),

    # -------------------Registration block-------------------
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='users/logout.html'),
        name='logout'),
    # ----------------------------------------------------------

    # -------------------Reset Password block-------------------
    path('registration/password_reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset_form.html',
                                              html_email_template_name='users/password_reset_email.html'),
         name='password_reset'),
    path('password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('password_change/',
         auth_views.PasswordChangeView.as_view(
             template_name='users/password_change_form.html'),
         name='password_change'),
    path('password_change_done/',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='users/password_change_done.html'),
         name='password_change_done'),
    # ----------------------------------------------------------
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
