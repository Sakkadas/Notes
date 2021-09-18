import pytest
from django.urls import reverse, reverse_lazy, resolve
from .factories import NotesFactory



@pytest.fixture
def note():
    return NotesFactory()

def test_list_resolve():
    """/ should resolve to notes:notes."""
    assert resolve('/').view_name == 'notes:notes'

# @pytest.mark.django_db
# def test_detail_reverse(note):
#     url = reverse('notes:note',
#                        kwargs={'slug': note.slug})
#     assert url == f'/view/{note.slug}/'

def test_add_resolve():
    """/notes/create/ should resolve to notes:create."""
    assert resolve('/create/').view_name == 'notes:create'