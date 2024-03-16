from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # URL para el admin de Django
    path('admin/', admin.site.urls),
    
    # URL para la aplicación app1
    path('', include('app1.urls')),
]

# Configuración para servir archivos multimedia en modo de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
