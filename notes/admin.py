from django.contrib import admin
from .models import *

from mptt.admin import MPTTModelAdmin


class NoteAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'summary', 'created', 'source', 'total_likes', ]
    list_filter = ('created', 'anonymous', )
    search_fields = ('author',)
    ordering = ('created',)

admin.site.register(Note, NoteAdmin)

admin.site.register(Comment, MPTTModelAdmin)
