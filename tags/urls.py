from django.urls import path

from .views import TagList

urlpatterns = [
    path('', TagList.as_view(), name='tags'),
]
