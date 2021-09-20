import pytest
import factory.fuzzy
from ..models import Note
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
from factory import Faker
from factory.django import DjangoModelFactory


pytestmark = pytest.mark.django_db

class UserFactory(DjangoModelFactory):
    username = Faker("user_name")
    email = Faker("email")

    class Meta:
        model = get_user_model()
        django_get_or_create = ["username"]


class NotesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Note
    author = factory.SubFactory(UserFactory)
    title = factory.fuzzy.FuzzyText()
    text = factory.fuzzy.FuzzyText()
    summary = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))
    tags = 'default'

@pytest.mark.django_db
def note():
    return NotesFactory()
