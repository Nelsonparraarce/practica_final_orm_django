from django.shortcuts import render, redirect, get_object_or_404

from .models import Laboratorio


def index(request):
    return render(request, 'index.html', {'index': index})

def mostrar_laboratorios(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'laboratorios.html', {'laboratorios': laboratorios})

# laboratorio/views.py
from .forms import LaboratorioForm

def agregar_laboratorio(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_laboratorios')
    else:
        form = LaboratorioForm()

    return render(request, 'agregar_laboratorio.html', {'form': form})

# laboratorio/views.py
def editar_laboratorio(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, pk=laboratorio_id)

    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('mostrar_laboratorios')
    else:
        form = LaboratorioForm(instance=laboratorio)

    return render(request, 'editar_laboratorio.html', {'form': form})

# laboratorio/views.py

def eliminar_laboratorio(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, pk=laboratorio_id)

    if request.method == 'POST':
        laboratorio.delete()
        return redirect('mostrar_laboratorios')

    return render(request, 'eliminar_laboratorio.html', {'laboratorio': laboratorio})
