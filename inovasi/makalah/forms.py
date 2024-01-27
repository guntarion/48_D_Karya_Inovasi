from django import forms
from .models import Makalah
from ckeditor.widgets import CKEditorWidget

class MakalahForm(forms.ModelForm):
    # abstrak = forms.CharField(widget=CKEditorWidget())
    # klaim = forms.CharField(widget=CKEditorWidget())
    # latar_belakang = forms.CharField(widget=CKEditorWidget())
    # maksud_tujuan = forms.CharField(widget=CKEditorWidget())
    # identifikasi_masalah = forms.CharField(widget=CKEditorWidget())
    # analisis_masalah = forms.CharField(widget=CKEditorWidget())
    # metodologi = forms.CharField(widget=CKEditorWidget())
    # desain_inovasi = forms.CharField(widget=CKEditorWidget())
    # implementasi = forms.CharField(widget=CKEditorWidget())
    # evaluasi_implementasi = forms.CharField(widget=CKEditorWidget())
    # manfaat_finansial = forms.CharField(widget=CKEditorWidget())
    # manfaat_non_finansial = forms.CharField(widget=CKEditorWidget())
    # daftar_pustaka = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Makalah
        fields = ('judul_makalah', 'kata_kunci', 'abstrak', 'kategori', 'klaim', 'latar_belakang', 'maksud_tujuan', 'identifikasi_masalah', 'analisis_masalah', 'metodologi', 'desain_inovasi', 'implementasi', 'evaluasi_implementasi', 'manfaat_finansial', 'manfaat_non_finansial', 'daftar_pustaka')
        widgets = {
            'judul_makalah': forms.TextInput(attrs={'placeholder': 'Judul Makalah', 'style': 'width:60%;'}),
            'kata_kunci': forms.TextInput(attrs={'placeholder': 'Kata Kunci', 'style': 'width:60%;'}),
            'abstrak': forms.Textarea(attrs={'placeholder': 'Abstrak makalah', 'style': 'width:60%;'}),
            'klaim': forms.Textarea(attrs={'placeholder': 'Klaim inovasi', 'style': 'width:60%;'}),
            'latar_belakang': forms.Textarea(attrs={'placeholder': 'Latar Belakang', 'style': 'width:60%;'}),
            'maksud_tujuan': forms.Textarea(attrs={'placeholder': 'Maksud dan tujuan', 'style': 'width:60%;'}),
            'identifikasi_masalah': forms.Textarea(attrs={'placeholder': 'Identifikasi masalah', 'style': 'width:60%;'}),
            'analisis_masalah': forms.Textarea(attrs={'placeholder': 'Analisis masalah', 'style': 'width:60%;'}),
            'metodologi': forms.Textarea(attrs={'placeholder': 'Metodologi', 'style': 'width:60%;'}),
            'desain_inovasi': forms.Textarea(attrs={'placeholder': 'Desain inovasi', 'style': 'width:60%;'}),
            'implementasi': forms.Textarea(attrs={'placeholder': 'Implementasi', 'style': 'width:60%;'}),
            'evaluasi_implementasi': forms.Textarea(attrs={'placeholder': 'Evaluasi Implementasi', 'style': 'width:60%;'}),
            'manfaat_finansial': forms.Textarea(attrs={'placeholder': 'Manfaat Finansial', 'style': 'width:60%;'}),
            'manfaat_non_finansial': forms.Textarea(attrs={'placeholder': 'Manfaat non Finansial', 'style': 'width:60%;'}),
            'daftar_pustaka': forms.Textarea(attrs={'placeholder': 'Daftar Pustaka', 'style': 'width:60%;'}),
        }