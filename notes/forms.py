from django import forms
from .models import *
from mptt.forms import TreeNodeChoiceField

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'title', 'text', 'image', 'source', 'summary', 'anonymous', 'tags',
        ]


class NewCommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['parent'].widget.attrs.update(
            {'class': 'd-none'})
        self.fields['parent'].label = ''
        self.fields['parent'].required = False

    class Meta:
        model = Comment
        fields = ('parent', 'email', 'text')

        widgets = {
            'email': forms.TextInput(attrs={'class': 'col-sm-12'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def save(self, *args, **kwargs):
        Comment.objects.rebuild()
        return super(NewCommentForm, self).save(*args, **kwargs)
