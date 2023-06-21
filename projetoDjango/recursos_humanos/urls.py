from django.urls import path
from . import views

urlpatterns = [
    path('recursos-humanos/', views.recursosHumanos, name="recursosHumanos"), 
]