from django.http import JsonResponse
from django.core import serializers
import json
from database.models import Cadastro #nome da classe do models de database

# Create your views here.
def parse_json(query_serializer):
    resposta_json = []
    for item in query_serializer:
        itens = {"nome": item['fields']['nome'],
                 "opcoes_funcoes": item['fields']['opcoes_funcoes'],
                 "email": item['fields']['email'],
                }
        resposta_json.append(itens)
    return resposta_json    

def view_registrar_cadastros(request):
    if request.method == 'POST':
        decode_json = request.body.decode('utf-8')
        registro_cadastro= json.loads(decode_json)
        banco = Cadastro(nome=registro_cadastro['nome'], opcoes_funcoes=registro_cadastro['opcoes_funcoes'], email=registro_cadastro['email'])
        banco.save()
        return JsonResponse({
            "status": "Cadastro Realizado com Sucesso",
            "registro": {
                "id": banco.pk,
                "nome":  registro_cadastro['nome'],
                "opcoes_funcoes": registro_cadastro['opcoes_funcoes'],
                "email": registro_cadastro['email'],
            }
        })
    elif request.method == 'GET':
        query_set = Cadastro.objects.all()
        query_serializer = serializers.serialize('json', query_set)
        nomes_json = json.loads(query_serializer)
        resposta_json = parse_json(nomes_json)
        return JsonResponse(resposta_json, safe=False)    
    elif request.method == 'PUT':
        decode_json = request.body.decode('utf-8')
        registro_cadastro = json.loads(decode_json)
        query_set = Cadastro.objects.get(pk=registro_cadastro['id'])
        query_set.nome = registro_cadastro['nome']
        query_set.opcoes_funcoes = registro_cadastro['opcoes_funcoes']
        query_set.email = registro_cadastro['email']
        query_set.save()
        return JsonResponse({
            "status": "Cadastro Atualizado com sucesso.",
            "registro": {
                "id": query_set.pk,
                "nome": query_set.nome,
                "opcoes_funcoes": query_set.opcoes_funcoes,
                "email": query_set.email,
            }
        })
    elif request.method == 'DELETE':
        decode_json = request.body.decode('utf-8')
        registro_financeiro = json.loads(decode_json)
        query_set = Cadastro.objects.get(pk=registro_financeiro['id'])
        query_set.delete()
        return JsonResponse({"status": "Dado excluído com sucesso."})

def view_buscar_cadastros(request, id):
    if request.method == 'GET':
        query_set = Cadastro.objects.get(pk=id)
        query_serialize = json.loads(serializers.serialize('json', [query_set]))
        resposta_json = parse_json(query_serialize)                                     
    return JsonResponse(resposta_json, safe=False)