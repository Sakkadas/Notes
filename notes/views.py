from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy, reverse

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from taggit.models import Tag

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

    def get_context_data(self, *args, **kwargs):
        context = super(NoteDetailView, self).get_context_data(**kwargs)
        note = get_object_or_404(Note, slug=self.kwargs['slug'])

        like_func = get_object_or_404(Note, slug=self.kwargs['slug'])
        total_likes = like_func.total_likes()

        liked = False
        if like_func.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['note'] = note
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

    def get_success_url(self):
        return reverse_lazy('notes:note', kwargs={'slug': self.object.slug})


def LikeView(request, slug):
    article = get_object_or_404(Note, slug=request.POST.get('post_slug'))
    liked = False
    if article.likes.filter(id=request.user.id).exists():
        article.likes.remove(request.user)
        liked = False
    else:
        article.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('notes:note', args=[str(slug)]))


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


class TaggedNoteListView(NotesListView):
    template_name = 'tags/tagged_list.html'

    def get_queryset(self):
        if 'tag_slug' in self.kwargs:
            slug = self.kwargs['tag_slug']
            tag = get_object_or_404(Tag, slug=slug)
            setattr(self, 'tag', tag)
        else:
            raise Http404('The tag slug wasn\'t found.')
        queryset = Note.objects.filter(tags=tag)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context
