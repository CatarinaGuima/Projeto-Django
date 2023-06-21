from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def financeiro(request):
    return HttpResponse("Bem-vindo(a) à página de financeiro")
