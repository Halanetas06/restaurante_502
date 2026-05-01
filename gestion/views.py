from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from .models import Cliente, Empleado, Mesa, Plato, Orden, Factura


def vista_login(request):
    if request.user.is_authenticated:
        return redirect('inicio')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('inicio')
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
    else:
        form = AuthenticationForm()
    
    return render(request, 'gestion/login.html', {'form': form})

def vista_registro(request):
    if request.user.is_authenticated:
        return redirect('inicio')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, "Cuenta creada exitosamente. Ahora puedes iniciar sesión.")
            return redirect('login')
        else:
            messages.error(request, "Error en el registro. Verifica los datos.")
    else:
        form = UserCreationForm()
    
    return render(request, 'gestion/registro.html', {'form': form})

def vista_logout(request):
    logout(request)
    return redirect('login')

def inicio(request):
    context = {
        'total_clientes': Cliente.objects.count(),
        'total_empleados': Empleado.objects.count(),
        'total_mesas': Mesa.objects.count(),
        'total_platos': Plato.objects.count(),
        'total_ordenes': Orden.objects.count(), 
        'total_facturas': Factura.objects.count(), 
    }
    return render(request, 'gestion/inicio.html', context)

def lista_clientes(request):

    clientes = Cliente.objects.all()
    return render(request, 'gestion/clientes.html', {'clientes': clientes})

def lista_empleados(request):

    empleados = Empleado.objects.all()
    return render(request, 'gestion/empleados.html', {'empleados': empleados})

def lista_mesas(request):

    mesas = Mesa.objects.all()
    return render(request, 'gestion/mesas.html', {'mesas': mesas})

def lista_platos(request):

    platos = Plato.objects.all()
    return render(request, 'gestion/platos.html', {'platos': platos})

def lista_ordenes(request):

    ordenes = Orden.objects.all()
    return render(request, 'gestion/ordenes.html', {'ordenes': ordenes})

def lista_facturas(request):
    
    facturas = Factura.objects.all()
    return render(request, 'gestion/facturas.html', {'facturas': facturas})