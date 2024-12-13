from django.shortcuts import render
from .models import RoomFacility

# Fungsi untuk halaman beranda
def home(request):
    return render(request, 'home.html')

# Fungsi untuk halaman fasilitas, mengambil semua data dari model RoomFacility
def fasilitas(request):
    facilities = RoomFacility.objects.all()  # Mengambil semua objek RoomFacility dari database
    return render(request, 'fasilitas.html', {'facilities': facilities})  # Menyertakan data fasilitas ke template

# Fungsi untuk halaman poliklinik
def poliklinik(request):
    return render(request, 'poliklinik.html')

# Fungsi untuk halaman lokasi
def lokasi(request):
    return render(request, 'lokasi.html')

# Fungsi untuk halaman kontak
def kontak(request):
    return render(request, 'kontak.html')
