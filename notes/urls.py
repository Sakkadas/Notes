from django.urls import path
from django.urls.conf import include
from .views import *

app_name = 'notes'

urlpatterns = [
    path("", NotesListView.as_view(), name='notes'),
    path("view/<str:slug>/", NotesDetailView.as_view(), name='note'),

]
