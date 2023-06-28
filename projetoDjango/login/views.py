from django.shortcuts import render
from django.http import JsonResponse
from database.models import Login
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
import json


# Create your views here.
def login(request):
    if request.method == 'POST':
        # Credenciais do usuário enviadas na solicitação
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verifica no banco de dados se o usuário existe
        try:
            user = Login.objects.get(username=username)
        except Login.DoesNotExist:
            # Usuário não existe
            return JsonResponse({'message': 'Usuário não encontrado'}, status=404)
        # validações e autenticação 
        if user.password == password:
            # Credenciais válidas
            return JsonResponse({'message': 'Login bem-sucedido'})
        else:
            # Credenciais inválidas
            return JsonResponse({'message': 'Login inválido'}, status=401)
    
    return render(request, 'login/login.html')

def parse_json(query_serializer):
    resposta_json = []
    for item in query_serializer:
        itens = {
                 "username": item['fields']['username'],
                 "password": item['fields']['password'],
                }
        resposta_json.append(itens)
    return resposta_json    

def view_registrar_usuarios(request):
    if request.method == 'POST':
        decode_json = request.body.decode('utf-8')
        registro_login = json.loads(decode_json)
        banco = Login(username=registro_login['username'], password=registro_login['password'])
        banco.save()
        return JsonResponse({
            "status": "Cadastro Realizado com Sucesso",
            "registro": {
                "id": banco.pk,
                "username":  registro_login['username'],
                "password": registro_login['password'],
            }
        })
    elif request.method == 'GET':
        query_set = Login.objects.all()
        query_serializer = serializers.serialize('json', query_set)
        nomes_json = json.loads(query_serializer)
        resposta_json = parse_json(nomes_json)
        return JsonResponse(resposta_json, safe=False)    
    elif request.method == 'PUT':
        decode_json = request.body.decode('utf-8')
        registro_login = json.loads(decode_json)
        query_set = Login.objects.get(pk=registro_login['id'])
        query_set.username = registro_login['username']
        query_set.password = registro_login['password']
        query_set.save()
        return JsonResponse({
            "status": "Cadastro Atualizado com sucesso.",
            "registro": {
                "id": query_set.pk,
                "username": query_set.username,
                "password": query_set.password,
            }
        })
    elif request.method == 'DELETE':
        decode_json = request.body.decode('utf-8')
        registro_login = json.loads(decode_json)
        query_set = Login.objects.get(pk=registro_login['id'])
        query_set.delete()
        return JsonResponse({"status": "Dado excluído com sucesso."})

def view_buscar_usuarios(request, id):
    if request.method == 'GET':
        try: 
            query_set = Login.objects.get(pk=id)
            query_serialize = json.loads(serializers.serialize('json', [query_set]))
            resposta_json = parse_json(query_serialize)      
            return JsonResponse(resposta_json, safe=False)                               
        except ObjectDoesNotExist:
            # Objeto não encontrado, retornar uma resposta adequada
            return JsonResponse({'error': 'ID não existe.'}, status=404)
     
