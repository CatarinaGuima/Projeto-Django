from django.urls import path
from . import views

urlpatterns = [
    path('financeiro/', views.view_registrar_financeiro, name="financeiro"), 
    path('financeiro/busca/<id>', views.view_buscar_financeiro, name="buscar_financeiro"),
]