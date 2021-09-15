import factory.django
import pytest
from django.contrib.auth.models import User
from factory import Faker
import factory.fuzzy
from django.template.defaultfilters import slugify
from ..models import Note


class NotesFactory(factory.django.DjangoModelFactory):
    # author = factory.SubFactory(AuthorFactory)
    title = factory.LazyAttribute(lambda obj: factory.Faker('title'))
    # text = factory.fuzzy.FuzzyText()
    # summary = factory.fuzzy.FuzzyText()
    # slug = factory.LazyAttribute(lambda obj: slugify(obj.name))
    # source = factory.LazyAttribute(lambda obj: f"https://{obj.name}")

    class Meta:
        model = Note


@pytest.fixture
def note():
    return NotesFactory()