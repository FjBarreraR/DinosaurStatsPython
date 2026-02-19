from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('cargar-datos/', views.importar_datos, name='cargar_datos'),
    path('dinosaurios/', views.lista_dinosaurios, name='listar_dinosaurios'),
]