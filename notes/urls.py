from django.urls import path
from django.urls.conf import include
from .views import *

app_name = 'notes'

urlpatterns = [
    path("", NotesListView.as_view(), name='notes'),
    path("view/<str:slug>/", NoteDetailView.as_view(), name='note'),
    path("create/", NoteCreateView.as_view(), name='create'),
    path("delete/<str:slug>/", NoteDeleteView.as_view(), name='delete'),
    path("update/<str:slug>/", NoteUpdateView.as_view(), name='update'),

]
