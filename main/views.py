from django.shortcuts import render

# Create our views here.
def mostrar_index(request):
    context={}
    return render(request, 'main/index.html',  context)

def mostrar_sesion(request):
    context={}
    return render(request,'main/sesion.html', context)

def mostrar_registrarse(request):
    context={}
    return render(request,'main/registrarse.html', context)

def mostrar_nosotros(request):
    context={}
    return render(request,'main/nostros.html', context)

def mostrar_jardineria(request):
    context={}
    return render(request,'main/jardineria.html', context)

def mostrar_herramientas(request):
    context={}
    return render(request,'main/herramientas.html', context)

def mostrar_carrito(request):
    context={}
    return render(request,'main/carrito.html', context)

