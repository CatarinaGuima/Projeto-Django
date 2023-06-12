from django.urls import path
from . import views

urlpatterns = [
    path("", views.obter_inicio, name="inicio")
]