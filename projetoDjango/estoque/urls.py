from django.urls import path
from . import views

urlpatterns = [
    path('estoque/', views.estoque, name="estoque"), 
]