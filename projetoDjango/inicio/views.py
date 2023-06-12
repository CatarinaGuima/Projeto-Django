from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def obter_inicio(request):
    return HttpResponse("Olá Tinoco Frut")