from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Rute untuk halaman admin
    path('admin/', admin.site.urls),

    # Rute untuk aplikasi 'hospital', mengarah ke file urls.py di aplikasi hospital
    path('', include('hospital.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
