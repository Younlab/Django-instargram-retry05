from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('postlist/', views.post_list, name='post-list'),
]