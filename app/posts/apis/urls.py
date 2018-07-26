from django.urls import path
from . import PostList
from . import generic_cbv as generic

urlpatterns = [
    # api view
    path('', PostList.as_view()),
    # generic_cbv view
    path('generic/', generic.PostList.as_view()),
    path('generic/user/', generic.UserList.as_view()),
]
