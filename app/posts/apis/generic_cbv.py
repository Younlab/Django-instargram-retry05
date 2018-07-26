from django.contrib.auth import get_user_model
from rest_framework import generics

from posts.serializers import PostSerializer, UserSerializer

from ..models import Post

User = get_user_model()

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer