from django.db import models
from ckeditor.fields import RichTextField
from PIL import Image
from django.utils.text import slugify

from taggit.managers import TaggableManager
from tags.models import UnicodeTaggedItem


class Note(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    text = RichTextField(blank=True, null=True)
    summary = models.CharField(max_length=100, default='', blank=True,
                               help_text='Describe article in nutshell')
    image = models.ImageField(blank=True, upload_to='picture_storage')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name="Url_slug")
    source = models.URLField(blank=True, default='',
                             help_text='If you want, put here your source link')
    anonymous = models.BooleanField(
        default=False, help_text='Others won\'t see that the note is yours.')
    tags = TaggableManager(
        through=UnicodeTaggedItem, blank=True,
        help_text='''Add tags. Separate tags by using "Enter" or comma.
           You can add maximum 5 tags, and length of tags should be less than 25
           symbols.''')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Note, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
