from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('demo/', include('demo.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
