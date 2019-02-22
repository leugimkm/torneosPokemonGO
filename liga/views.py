from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Q

def index(request):
    datos = [{
        'autor':'mkm',
        'titulo':'inicio'
    }]
    context = {
        'mostrar': datos
    }
    return render(request, 'liga/index.html', context)

def reglas(request):
    return render(request, 'liga/reglas.html')

def lista(request):
    entrenadores = User.objects.all()
    context = {
        'entrenadores': entrenadores,
    }
    return render(request, 'liga/lista.html', context)

def buscar(request):
    query = request.GET.get('q')
    results = User.objects.filter(Q(username__contains=query))
    context = {
        'results': results,
    }
    return render(request, 'liga/buscar.html',context)
