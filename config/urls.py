from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    path('', include('notes.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),

]
