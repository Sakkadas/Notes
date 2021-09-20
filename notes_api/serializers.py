from rest_framework import serializers
from notes.models import Note, Comment


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = (
            'author', 'title',
            'summary', 'created',
            'updated', 'slug', 'source',
            'anonymous', 'total_likes',
        )


class NoteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = (
            'author', 'title', 'text',
            'image', 'created',
            'updated', 'slug', 'source',
            'anonymous', 'total_likes',
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'note', 'author', 'parent',
            'text', 'email', 'publish',
            'status',
        )
