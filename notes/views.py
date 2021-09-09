from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import *


class NotesListView(ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'


class NotesDetailView(DetailView):
    model = Note
    template_name = 'notes/notes_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(NotesDetailView, self).get_context_data(**kwargs)
        note = get_object_or_404(Note, slug=self.kwargs['slug'])
        context['note'] = note
