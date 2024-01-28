from django.shortcuts import render, redirect, get_object_or_404
from .models import Makalah, Masukan
from .forms import MakalahForm, MasukanForm, MasukanFollowUpForm

def makalah_home(request):
    makalahs = Makalah.objects.all()
    return render(request, 'inovasi/makalah-home.html', {'makalahs': makalahs})

def makalah_create(request):
    if request.method == 'POST':
        form = MakalahForm(request.POST, request.FILES)
        if form.is_valid():
            makalah = form.save(commit=False)
            makalah.penyusun = request.user
            makalah.save()
            form.save_m2m()  # save many-to-many fields
            return redirect('makalah_home')
    else:
        form = MakalahForm()
    return render(request, 'inovasi/makalah-create.html', {'form': form})

def makalah_edit(request, makalah_id):
    makalah = get_object_or_404(Makalah, id=makalah_id)
    if request.method == 'POST':
        form = MakalahForm(request.POST, request.FILES, instance=makalah)
        if form.is_valid():
            makalah = form.save(commit=False)
            makalah.save()
            form.save_m2m()  # save many-to-many fields
            return redirect('makalah_single_view', makalah_id=makalah.id)
    else:
        form = MakalahForm(instance=makalah)
    return render(request, 'inovasi/makalah-create.html', {'form': form})

def makalah_single_view(request, makalah_id):
    makalah = get_object_or_404(Makalah, id=makalah_id)
    if request.method == 'POST':
        form_masukan = MasukanForm(request.POST)
        if form_masukan.is_valid():
            masukan = form_masukan.save(commit=False)
            masukan.pemberi_masukan = request.user
            masukan.makalah = makalah
            masukan.save()
    else:
        form_masukan = MasukanForm()
    return render(request, 'inovasi/makalah-single-view.html', {'makalah': makalah, 'form_masukan': form_masukan})


def masukan_home(request):
    masukans = Masukan.objects.all()
    return render(request, 'inovasi/masukan-home.html', {'masukans': masukans})


def masukan_single_view(request, masukan_id):
    masukan = get_object_or_404(Masukan, id=masukan_id)
    if request.method == 'POST':
        form = MasukanFollowUpForm(request.POST, instance=masukan)
        if form.is_valid():
            instance = form.save(commit=False)
            for attr, value in form.cleaned_data.items():
                # this is to prevent overwriting the existing data with blank data from the form
                if attr not in ['judul_masukan', 'isi_masukan']:
                    setattr(instance, attr, value)
            instance.status_masukan = 'done'
            instance.save()
    else:
        form = MasukanFollowUpForm(instance=masukan)
    return render(request, 'inovasi/masukan-single-view.html', {'form': form, 'masukan': masukan})
