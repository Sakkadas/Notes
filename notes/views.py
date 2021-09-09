from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import *


class NotesListView(ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'


class NotesDetailView(DetailView):
    model = Note
    template_name = 'notes/note_view.html'

    def get_context_data(self, *args, **kwargs):
        context = super(NotesDetailView, self).get_context_data(**kwargs)
        note = get_object_or_404(Note, slug=self.kwargs['slug'])
        context['note'] = note

class NotesCreateView(CreateView):
    model = Note
    success_url = reverse_lazy('notes')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(NotesCreateView, self).form_valid(form)

class NoteUpdateView(UpdateView):
    model = Note
    template_name = 'notes/update_note.html'

class NotesDeleteView(DeleteView):
    model = Note
    template_name = 'notes/delete_note.html'
    success_url = reverse_lazy('notes')
    context_object_name = 'notes'