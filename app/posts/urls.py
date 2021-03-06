from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('postcreate/', views.post_create, name='post-create'),
    path('<int:pk>/postdelete/', views.post_delete, name='post-delete'),
]
