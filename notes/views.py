from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy, reverse

from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from taggit.models import Tag

from .models import *
from .forms import *


class NotesListView(ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    paginate_by = 6

    def get_order(self):
        order = self.request.GET.get('order', '-created')
        if order.replace('-', '', 1) == 'created':
            return order
        return '-created'

    def get_queryset(self):
        queryset = Note.feature.filter(anonymous=False)
        if self.request.user.is_authenticated:
            user = self.request.user
            personal_queryset = Note.feature.get_personal_notes(user)
            queryset = queryset | personal_queryset
        order = self.get_order()
        return queryset.order_by(order)


class PersonalNotesList(LoginRequiredMixin, NotesListView):
    template_name = 'notes/personal_notes.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = Note.feature.get_personal_notes(self.request.user)
        order = self.get_order()
        return queryset.order_by(order)


class NoteDetailView(FormMixin, DetailView):
    model = Note
    template_name = 'notes/note_view.html'
    form_class = NewCommentForm

    def get_context_data(self, *args, **kwargs):
        context = super(NoteDetailView, self).get_context_data(**kwargs)
        note = get_object_or_404(Note, slug=self.kwargs['slug'])

        like_func = get_object_or_404(Note, slug=self.kwargs['slug'])
        total_likes = like_func.total_likes()

        comments = note.comments.filter(status=True)
        comment_form = NewCommentForm(initial={'notes:note': self.object})

        liked = False
        if like_func.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['comments'] = comments
        context['comment_form'] = comment_form
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

    def get_success_url(self):
        return reverse_lazy('notes:note', kwargs={'slug': self.object.slug})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, **kwargs):
        form.instance.author = self.request.user
        form.instance.note = self.object
        form.save()
        return super().form_valid(form)


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


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    success_url = reverse_lazy('notes:notes')
    form_class = NoteForm
    context_object_name = 'note'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(NoteCreateView, self).form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    success_url = reverse_lazy('notes:notes')
    form_class = NoteForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NoteDeleteView(LoginRequiredMixin, DeleteView):
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
        queryset = Note.feature.filter(tags=tag)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context


def note_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
        search_vector = SearchVector('title', 'text')
        search_query = SearchQuery(query)
        results = Note.published.annotate(
            search=search_vector,
            rank=SearchRank(search_vector, search_query)
        ).filter(search=search_query).order_by('-rank')
    return render(request, 'notes/search.html',
                  {'form': form,
                   'query': query,
                   'results': results})
