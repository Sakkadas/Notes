from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from notes.models import Note, Comment
from .serializers import NoteSerializer, CommentSerializer
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser


class NotesViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser, JSONParser,)
    queryset = Note.feature.all()
    serializer_class = NoteSerializer


class CommentViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser, JSONParser,)
    permission_classes = IsAuthenticated
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
