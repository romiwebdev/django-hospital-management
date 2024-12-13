from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),           # URL untuk halaman beranda, akan memanggil views.home
    path('fasilitas/', views.fasilitas, name='fasilitas'),  # URL untuk halaman fasilitas, akan memanggil views.fasilitas
    path('poliklinik/', views.poliklinik, name='poliklinik'),  # URL untuk halaman poliklinik, akan memanggil views.poliklinik
    path('lokasi/', views.lokasi, name='lokasi'),  # URL untuk halaman lokasi, akan memanggil views.lokasi
    path('kontak/', views.kontak, name='kontak'),  # URL untuk halaman kontak, akan memanggil views.kontak
]
