# forms.py
from django import forms
from .models import Ideasi

class IdeasiForm(forms.ModelForm):
    nama_ide = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'width:30%;', 'id': 'nama_ide'}))
    latar_belakang_ide = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'style': 'width:30%;', 'placeholder': 'Latar belakang'}))
    ide_solusi = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'style': 'width:30%;', 'placeholder': 'Latar belakang'}))
    class Meta:
        model = Ideasi
        fields = ['nama_ide', 'latar_belakang_ide', 'ide_solusi']