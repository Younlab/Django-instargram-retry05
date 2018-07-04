from django.urls import path
from . import views

app_name = 'members'
urlpatterns = [
    path('signin/', views.sign_in, name='sign-in'),
]
