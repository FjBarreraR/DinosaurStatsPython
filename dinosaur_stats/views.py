from django.shortcuts import render
from .services import obtener_dinosaurios

# Create your views here.
def home(request):
    return render(request, 'home/home.html')
def lista_dinosaurios(request):
    datos_api = obtener_dinosaurios()

    return render(request, 'dinosaurios/mostrar_dinos.html', {
        'datos_api': datos_api
    })