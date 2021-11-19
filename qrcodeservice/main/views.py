from django.shortcuts import render
from .models import Qrcodes
from .forms import QrcodesForm


def index(request):
    qrcodes = Qrcodes.objects.all()
    return render(request, 'main/index.html', {'qrcodes': qrcodes})


def create(request):
    error = ""
    if request.method == 'POST':
        form = QrcodesForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма была неверной'
    form = QrcodesForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

