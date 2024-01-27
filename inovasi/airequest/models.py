from django.db import models
from core.models import TimeStampedModel
from django.conf import settings

KATEGORI_UMUM_CHOICES = [
    ('pertanyaan', 'Ajukan Pertanyaan'),
    ('kritikan', 'Kritikan'),
    ('saran_pengembangan', 'Saran Pengembangan'),
    ('catatan_kritis_umum', 'Catatan Kritis Umum'),
    ('catatan_kritis_aplikasi', 'Catatan Kritis Aplikasi'),
    ('ide_manfaat_inovasi', 'Ide Manfaat Inovasi'),
    ('ide_risiko_inovasi', 'Ide Risiko Inovasi'),
    ('ide_risiko_inovasi_softwarefull', 'Ide Risiko Inovasi Software Full'),
    ('ide_risiko_inovasi_softwarealat', 'Ide Risiko Inovasi Software dengan Alat'),
    ('analisis_latar_belakang', 'Analisis Latar Belakang'),
    ('analisis_metodologi', 'Analisis Metodologi'),
]



class OpenAIRequest(TimeStampedModel):
    pembuat_request = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="pembuat_request"
    )
    pembuat_username = models.CharField(max_length=150)
    kategori_umum = models.CharField(
        max_length=240, choices=KATEGORI_UMUM_CHOICES, null=True, blank=True)
    input_request = models.TextField(null=True, blank=True)
    output_request = models.TextField(null=True, blank=True)
    prompt_tokens = models.IntegerField(default=0)
    completion_tokens = models.IntegerField(default=0)
    total_tokens = models.IntegerField(default=0)
    input_words_count = models.IntegerField(default=0)
    output_words_count = models.IntegerField(default=0)

    def __str__(self):
        return self.kategori_spesifik + ' | ' + self.kategori_spesifik
