from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    path('tags/', include(('tags.urls', 'tags'), namespace='tags')),
    path('', include('notes.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('notes_api/', include('notes_api.urls')),
]
