
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('main.urls')) 
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#импорт папки с фото
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
