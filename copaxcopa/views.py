from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

def costeo(request):
    return render(request, 'costeo.html')

def recetas(request):
    return render(request, 'recetas.html')
