from django.urls import path
from . import views

urlpatterns = [
    path('recursoshumanos/', views.recursosHumanos, name="recursosHumanos"), 
]