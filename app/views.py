from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor
from .forms import ProveedorForm
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'app/index.html')

def contacto(request):
    return render(request, 'app/contacto.html')

def formulario_enviado(request):
    return render(request, 'app/formulario-enviado.html')

def seccion_gatos(request):
    return render(request, 'app/seccion-gatos.html')

def seccion_perros(request):
    return render(request, 'app/seccion-perros.html')

def proveedores(request):
    proveedores = Proveedor.objects.all()
    data = {
        'proveedores': proveedores
    }
    return render(request, 'app/proveedores/proveedores.html', data)

def agregar_proveedor(request):

    data = {
        'form': ProveedorForm()
    }

    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Proveedor registrado")
        else:
            data["form"] = formulario
    return render(request, 'app/proveedores/agregar.html', data)

def listar_proveedor(request):
    proveedores = Proveedor.objects.all()
    data = {
        'proveedores': proveedores
    }
    return render(request, 'app/proveedores/listar.html', data)

def modificar_proveedor(request, id):

    proveedores = get_object_or_404(Proveedor,rut= id)
    #producto = Producto.objects.get(id_producto=id)

    data = {
        'form' : ProveedorForm(instance=proveedores)
    }

    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST, instance=proveedores)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificado correctamente")
            return redirect(to="listar_proveedor")
        else:
            data["form"] = formulario
    return render (request, 'app/proveedores/modificar.html', data)

def eliminar_proveedor(request, id):

    proveedores = get_object_or_404(Proveedor, rut=id)
    proveedores.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_proveedor")

