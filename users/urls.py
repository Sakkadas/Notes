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
        template_name='account/logout.html'),
         name='logout'),
    # ----------------------------------------------------------

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
