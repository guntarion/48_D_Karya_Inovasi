from django.db import models
from django.conf import settings
from django.utils.text import slugify

from core.models import TimeStampedModel


class Makalah(TimeStampedModel):
    judul_makalah = models.CharField(max_length=255)
    penyusun = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="penyusun"
    )

    KATEGORI_CHOICES = [
        ('aplikasi_murni', 'Aplikasi Murni'),
        ('aplikasi_alat', 'Aplikasi dengan Alat'),
        ('technical_support', 'Technical Support'),
        ('bebas', 'Bebas'),
    ]
    kategori = models.CharField(
        max_length=255,
        choices=KATEGORI_CHOICES,
        default='Bebas',
    )
    abstrak = models.TextField(blank=True, null=True)
    kata_kunci = models.CharField(max_length=255)
    klaim = models.TextField(blank=True, null=True)
    latar_belakang = models.TextField(blank=True, null=True)
    maksud_tujuan = models.TextField(blank=True, null=True)
    identifikasi_masalah = models.TextField(blank=True, null=True)
    analisis_masalah = models.TextField(blank=True, null=True)
    metodologi = models.TextField(blank=True, null=True)
    desain_inovasi = models.TextField(blank=True, null=True)
    implementasi = models.TextField(blank=True, null=True)
    evaluasi_implementasi = models.TextField(blank=True, null=True)
    manfaat_finansial = models.TextField(blank=True, null=True)
    manfaat_non_finansial = models.TextField(blank=True, null=True)
    daftar_pustaka = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    
    note_pertanyaan = models.TextField(blank=True, null=True)
    note_latar_belakang = models.TextField(blank=True, null=True)
    note_manfaat_inovasi = models.TextField(blank=True, null=True)
    note_risiko_fullsoftware = models.TextField(blank=True, null=True)
    note_risiko_software_alat = models.TextField(blank=True, null=True)
    note_metodologi = models.TextField(blank=True, null=True)
    note_kriteria_latar_belakang = models.TextField(blank=True, null=True)
    note_kriteria_metodologi = models.TextField(blank=True, null=True)
    note_penerapan_inovasi = models.TextField(blank=True, null=True)
    note_evaluasi_hasil = models.TextField(blank=True, null=True)
    note_kontribusi_manfaat = models.TextField(blank=True, null=True)
    note_keunggulan_inovasi = models.TextField(blank=True, null=True)
    note_pengembangan = models.TextField(blank=True, null=True)
    note_kemudahan_implementasi = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.judul_makalah)
            original_slug = self.slug
            counter = 1

            while Makalah.objects.filter(slug=self.slug).exists():
                self.slug = '{}-{}'.format(original_slug, counter)
                counter += 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.judul_makalah

