from django.db import models
from core.models import TimeStampedModel


class Ideasi(TimeStampedModel):
    nama_ide = models.CharField(max_length=255)
    latar_belakang_ide = models.TextField(blank=True, null=True)
    ide_solusi = models.TextField(blank=True, null=True)

