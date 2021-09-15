from .factories import NotesFactory, note
import pytest


@pytest.mark.django_db
def test_note_detail_view(rf, note):
    note = NotesFactory()
