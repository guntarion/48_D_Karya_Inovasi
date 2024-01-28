from django.contrib import admin
from .models import Makalah, Masukan

class MakalahAdmin(admin.ModelAdmin):
    list_display = ('judul_makalah', 'penyusun', 'kategori')  # Add more fields as needed
    search_fields = ['judul_makalah', 'penyusun__username']  # Add more fields as needed

admin.site.register(Makalah, MakalahAdmin)

class MasukanAdmin(admin.ModelAdmin):
    list_display = ['isi_masukan', 'status_masukan', 'pemberi_masukan', 'makalah']
    search_fields = ['isi_masukan', 'status_masukan', 'pemberi_masukan__username', 'makalah__title']
    list_filter = ['status_masukan']

admin.site.register(Masukan, MasukanAdmin)