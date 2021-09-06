from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('User/', include(('apps.users.urls','users'))),
    path('Post/', include(('apps.posts.urls','posts'))),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)