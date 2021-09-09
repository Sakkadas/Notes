from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy, reverse


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import *
from .forms import *


class NotesListView(ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    success_url = reverse_lazy('notes:notes')


class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/note_view.html'
    context_object_name = 'note'

    def get_context_data(self, *args, **kwargs):
        context = super(NoteDetailView, self).get_context_data(**kwargs)
        note = get_object_or_404(Note, slug=self.kwargs['slug'])
        context['note'] = note


class NoteCreateView(CreateView):
    model = Note
    success_url = reverse_lazy('notes:notes')
    form_class = NoteForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(NoteCreateView, self).form_valid(form)


class NoteUpdateView(UpdateView):
    model = Note
    success_url = reverse_lazy('notes:notes')
    form_class = NoteForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'notes/note_delete.html'
    success_url = reverse_lazy('notes:notes')
    context_object_name = 'note'
