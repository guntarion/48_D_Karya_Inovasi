from django.shortcuts import render, redirect, get_object_or_404
from .models import Makalah
from .forms import MakalahForm  # make sure you have this form

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
    return render(request, 'inovasi/makalah-single-view.html', {'makalah': makalah})