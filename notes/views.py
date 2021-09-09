from django.shortcuts import render
from django.views.generic.list import ListView

from .models import *


class NotesListView(ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'notes_list.html'
