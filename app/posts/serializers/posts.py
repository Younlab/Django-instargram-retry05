from rest_framework import serializers

from posts.models import Post

__all__ = (
    'PostSerializer',
)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'author',
            'image',
            'content',
            'created_at',
        )