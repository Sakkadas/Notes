from django.contrib import admin
from .models import *

from mptt.admin import MPTTModelAdmin


class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Note, NoteAdmin)

admin.site.register(Comment, MPTTModelAdmin)
