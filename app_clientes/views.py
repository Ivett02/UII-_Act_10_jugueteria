from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Cliente
from .forms import ClienteForm

def index(request):
    clientes = Cliente.objects.all()
    return render(request, 'app_clientes/index.html', {'clientes': clientes})

def view_cliente(request, id):
    cliente = Cliente.objects.get(pk=id)
    # Por ahora solo redirige al index
    return redirect('index')

def add(request):
    success = False

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = ClienteForm()  # formulario vacío después de guardar
    else:
        form = ClienteForm()  # formulario vacío para GET

    return render(request, 'app_clientes/add.html', {
        'form': form,
        'success': success
    })

def edit(request, id):
    cliente = Cliente.objects.get(pk=id)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            # recarga el formulario con los datos actualizados
            form = ClienteForm(instance=cliente)
            success = True
        else:
            success = False
    else:
        form = ClienteForm(instance=cliente)
        success = False

    return render(request, 'app_clientes/edit.html', {
        'form': form,
        'success': success
    })

def delete(request, id):
    if request.method == 'POST':
        cliente = Cliente.objects.get(pk=id)
        cliente.delete()
    return redirect('index')