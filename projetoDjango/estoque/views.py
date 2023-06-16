from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def estoque(request):
    return HttpResponse("Bem-vindo(a) à página de estoque")
