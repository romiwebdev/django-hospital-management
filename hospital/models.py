from django.db import models

class RoomFacility(models.Model):
    # Daftar tipe kamar yang bisa dipilih
    ROOM_TYPES = [
        ('Kelas 1', 'Kelas 1'),
        ('Executive', 'Executive'),
        ('VIP', 'VIP'),
    ]
    
    # Menyimpan tipe kamar, pilihannya ada di ROOM_TYPES
    room_type = models.CharField(max_length=50, choices=ROOM_TYPES)
    
    # Menyimpan fitur ruangan, dipisahkan dengan koma
    features = models.TextField(help_text="Masukkan fitur, pisahkan dengan koma (contoh: AC, TV LED, Wi-Fi gratis)")
    
    # Menyimpan gambar ruangan, bisa kosong
    image = models.ImageField(upload_to='room_images/', blank=True, null=True)

    # Mengembalikan daftar fitur dalam bentuk list
    def feature_list(self):
        return [feature.strip() for feature in self.features.split(',')]

    # Menampilkan tipe kamar saat objek dipanggil sebagai string
    def __str__(self):
        return self.room_type
