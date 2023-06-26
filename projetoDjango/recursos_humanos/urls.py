from django.urls import path
from . import views

urlpatterns = [
    path('recursos-humanos/', views.view_registrar_recursosHumanos, name="recursosHumanos"), 
    path('recursos-humanos/busca/<id>', views.view_buscar_recursosHumanos, name="buscar_recursosHumanos")
]