from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginScreen, name="login"), 
]