from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown
from ..models import Note

register = template.Library()


@register.simple_tag
def total_notes():
    return Note.published.count()

@register.simple_tag
def get_most_commented_notes(count=5):
    return Note.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
