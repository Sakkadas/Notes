from django.db import models
from ckeditor.fields import RichTextField
from PIL import Image
from django.utils.text import slugify
from django.contrib.auth.models import User

from taggit.managers import TaggableManager
from tags.models import UnicodeTaggedItem

from mptt.models import MPTTModel, TreeForeignKey


class Note(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    text = RichTextField(blank=True, null=True)
    summary = models.CharField(max_length=100, default='', blank=True,
                               help_text='Describe article in nutshell')
    image = models.ImageField(blank=True, upload_to='picture_storage')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, blank=True)
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name="Url_slug")
    source = models.URLField(blank=True, default='',
                             help_text='If you want, put here your source link')
    anonymous = models.BooleanField(
        default=False, help_text='Others won\'t see that the note is yours.')
    tags = TaggableManager(
        through=UnicodeTaggedItem, blank=True,
        help_text='''Put your tags here in order to help people find interesting issue.
                    You able to add 5 tags.
                    Length must be less than 25 symbols.''')

    def total_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Note, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(MPTTModel):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Comment')
    email = models.EmailField(blank=True)
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ['publish']

    def __str__(self):
        return self.text