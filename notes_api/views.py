from django.shortcuts import render
from rest_framework import viewsets
from notes.models import Note
from .serializers import NoteSerializer
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser



class NotesViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser, JSONParser,)
    queryset = Note.feature.all()
    serializer_class = NoteSerializer
