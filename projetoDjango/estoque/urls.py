from django.urls import path
from . import views

urlpatterns = [
    path('estoque/', views.view_registrar_estoque, name="estoque"), 
    path('estoque/busca/<id>', views.view_buscar_estoque, name="buscar_estoque"),
]
