from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.view_registrar_cadastros, name="cadastro"), 
    path('cadastro/busca/<id>', views.view_buscar_cadastros, name="buscar_cadastros"),
]