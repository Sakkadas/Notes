from django.urls import path

from .views import TagList

app_name = 'tags'
urlpatterns = [
    path('', TagList.as_view(), name='tags'),
]
