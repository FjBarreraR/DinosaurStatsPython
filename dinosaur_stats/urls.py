from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dinosaurios/', views.lista_dinosaurios, name='listar_dinosaurios'),
]