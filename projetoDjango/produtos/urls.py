from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.view_registrar_produtos, name="produtos"), 
    path('produtos/busca/<id>', views.view_buscar_produtos, name="buscar_produtos")
]