from django.urls import path
from django.urls.conf import include
from .views import *

app_name = 'notes'

urlpatterns = [
    # -------------------------CRUD-------------------------
    path("", NotesListView.as_view(), name='notes'),
    path("view/<str:slug>/", NoteDetailView.as_view(), name='note'),
    path("create/", NoteCreateView.as_view(), name='create'),
    path("delete/<str:slug>/", NoteDeleteView.as_view(), name='delete'),
    path("update/<str:slug>/", NoteUpdateView.as_view(), name='update'),
    # -------------------------------------------------------
    
    path('personal/', PersonalNotesList.as_view(), name='personal'),
    path('tag/<str:tag_slug>/', TaggedNoteListView.as_view(), name='tagged'),
    path("like/<str:slug>/", LikeView, name='like'),

]
