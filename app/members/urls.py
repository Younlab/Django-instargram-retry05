from django.urls import path
from . import views

app_name = 'members'
urlpatterns = [
    path('signin/', views.sign_in, name='sign-in'),
    path('signout/', views.sign_out, name='sign-out'),
]
