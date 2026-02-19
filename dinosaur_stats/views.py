import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.db import IntegrityError
from django.shortcuts import render, redirect
from .services import obtener_dinosaurios
from .models import Dinosaur
from django.contrib.auth.models import User


# Create your views here.

# CARGAR DATOS
def importar_datos(request):
    if request.method == 'POST':
        url = 'https://dinoapi.brunosouzadev.com/api/dinosaurs'
        try:
            response = requests.get(url)
            datos = response.json()

            if response.status_code == 200:
                for item in datos:
                    Dinosaur.objects.update_or_create(
                        code = item['_id'],
                        defaults={
                            'name': item['name'],
                            'weight': item['weight'],
                            'height': item['height'],
                            'length': item['length'],
                            'diet': item['diet'],
                            'period': item['period'],
                            'existed': item['existed'],
                            'region': item['region'],
                            'type': item['type'],
                            'description': item['description'],
                            'image': item['image'],
                    })

                messages.success(request, f"¡Sincronización completa! {len(datos)} procesados.")
        except requests.exceptions.RequestException as e:
            return redirect('home/home.html')
    return render(request, 'load_data/cargar_datos.html')

# REGISTRO
def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password
            )
            messages.success(request, 'Cuenta creada con éxito!')
            return redirect('login')

        except IntegrityError:
            messages.error(request, 'Este correo ya está registrado!')

    return render(request, 'user/register.html')

# LOGIN
def login(request):
    if request.method == 'POST':
        email = request.POST['email'] or request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Credenciales no validas!')

    return render(request, 'user/login.html')

def logout(request):
    auth_logout(request)
    messages.info(request, 'Has cerrado sesión')
    return redirect('home')

# DINOSAURIOS
def lista_dinosaurios(request):
    datos_api = obtener_dinosaurios()

    return render(request, 'dinosaurios/mostrar_dinos.html', {
        'datos_api': datos_api
    })

# HOME
def home(request):
    return render(request, 'home/home.html')