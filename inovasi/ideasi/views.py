# views.py
from django.shortcuts import render, redirect
from .forms import IdeasiForm

def create_ideasi(request):
    if request.method == 'POST':
        form = IdeasiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('makalah_home')
    else:
        form = IdeasiForm()
    return render(request, 'inovasi/ideasi-create.html', {'form': form})