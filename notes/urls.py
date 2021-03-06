from django.urls import path
from django.urls.conf import include

from django.conf import settings
from django.conf.urls.static import static

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
    path('search/', note_search, name='note_search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
