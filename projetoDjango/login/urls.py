from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"), 
    path('login/contas', views.view_registrar_usuarios, name="contas"), 
    path('login/contas/busca/<id>', views.view_buscar_usuarios, name="buscar_contas"), 
]