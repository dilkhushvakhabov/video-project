from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from account.views import LoginAPIView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')),
    path('login/', LoginAPIView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
