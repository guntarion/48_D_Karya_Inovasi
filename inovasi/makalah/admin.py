from django.contrib import admin
from .models import Makalah

class MakalahAdmin(admin.ModelAdmin):
    list_display = ('judul_makalah', 'penyusun', 'kategori')  # Add more fields as needed
    search_fields = ['judul_makalah', 'penyusun__username']  # Add more fields as needed

admin.site.register(Makalah, MakalahAdmin)