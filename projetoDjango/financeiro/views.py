from django.http import JsonResponse
from django.core import serializers
import json
from database.models import Financeiro #nome da classe do models de database

# Create your views here.
def parse_json(query_serializer):
    resposta_json = []
    for item in query_serializer:
        itens = {
                 "tipo": item['fields']['tipo'],
                 "status": item['fields']['status'],
                 "data": item['fields']['data'],
                 "descricao": item['fields']['descricao'],
                 "valor": item['fields']['valor'],
                }
        resposta_json.append(itens)
    return resposta_json    

def view_registrar_financeiro(request):
    if request.method == 'POST':
        decode_json = request.body.decode('utf-8')
        registro_financeiro= json.loads(decode_json)
        banco = Financeiro(tipo=registro_financeiro['tipo'], status=registro_financeiro['status'], data=registro_financeiro['data'], descricao=registro_financeiro['descricao'], valor=registro_financeiro['valor'])
        banco.save()
        return JsonResponse({
            "status": "Cadastro Realizado com Sucesso",
            "registro": {
                "id": banco.pk,
                "tipo": registro_financeiro['tipo'],
                "status": registro_financeiro['status'],
                "data": registro_financeiro['data'],
                "descricao": registro_financeiro['descricao'],
                "valor": registro_financeiro['valor'],
            }
        })
    elif request.method == 'GET':
        query_set = Financeiro.objects.all()
        query_serializer = serializers.serialize('json', query_set)
        nomes_json = json.loads(query_serializer)
        resposta_json = parse_json(nomes_json)
        return JsonResponse(resposta_json, safe=False)    
    elif request.method == 'PUT':
        decode_json = request.body.decode('utf-8')
        registro_financeiro = json.loads(decode_json)
        query_set = Financeiro.objects.get(pk=registro_financeiro['id'])
        query_set.tipo = registro_financeiro['tipo']
        query_set.status = registro_financeiro['status']
        query_set.data = registro_financeiro['data']
        query_set.descricao = registro_financeiro['descricao']
        query_set.valor = registro_financeiro['valor']
        query_set.save()
        return JsonResponse({
            "status": "Cadastro Atualizado com sucesso.",
            "registro": {
                "id": query_set.pk,
                "tipo": query_set.tipo,
                "status": query_set.status,
                "data":  query_set.data,
                "descricao":  query_set.descricao,
                "valor":  query_set.valor
            }
        })
    elif request.method == 'DELETE':
        decode_json = request.body.decode('utf-8')
        registro_financeiro = json.loads(decode_json)
        query_set = Financeiro.objects.get(pk=registro_financeiro['id'])
        query_set.delete()
        return JsonResponse({"status": "Dado excluído com sucesso."})

def view_buscar_financeiro(request, id):
    if request.method == 'GET':
        query_set = Financeiro.objects.get(pk=id)
        query_serialize = json.loads(serializers.serialize('json', [query_set]))
        resposta_json = parse_json(query_serialize)                                     
    return JsonResponse(resposta_json, safe=False)