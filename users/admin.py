from django.contrib import admin
from .models import Profile
from notes.models import Comment


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user',]


admin.site.register(Profile, ProfileAdmin)
