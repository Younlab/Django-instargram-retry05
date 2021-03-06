from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from members import apis
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('members.urls')),
    path('post/', include('posts.urls')),
    path('', views.index, name='index'),
    path('api/posts/', include('posts.apis.urls')),
    path('api/users/', apis.UserList.as_view()),
]

urlpatterns += static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,

)
