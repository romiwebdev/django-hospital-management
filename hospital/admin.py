from django.contrib import admin
from .models import RoomFacility

# Mendaftarkan model RoomFacility ke admin Django dengan kustomisasi tampilan
@admin.register(RoomFacility)
class RoomFacilityAdmin(admin.ModelAdmin):
    # kolom yang ditampilkan di daftar objek RoomFacility di admin
    list_display = ('room_type', 'features')

    # fitur pencarian berdasarkan field room_type
    search_fields = ('room_type',)
