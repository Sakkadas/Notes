import pytest
from ..models import Note
from .factories import NotesFactory

pytestmark = pytest.mark.django_db

@pytest.mark.django_db
def test___str__():
    note = NotesFactory()
    assert note.__str__() == note.title
    assert str(note) == note.title
