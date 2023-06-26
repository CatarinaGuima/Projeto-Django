from django.http import JsonResponse
from django.core import serializers
import json
from database.models import RecursosHumano #nome da classe do models de database

# Create your views here.
def parse_json(query_serializer):
    resposta_json = []
    for item in query_serializer:
        itens = {
                 "funcionario": item['fields']['funcionario'],
                 "cargo": item['fields']['cargo'],
                 "salario": item['fields']['salario'],
                 "carga_horaria": item['fields']['carga_horaria'],
                 "folha_de_ponto": item['fields']['folha_de_ponto'],
                 "setor": item['fields']['setor']
                }
        resposta_json.append(itens)
    return resposta_json    

def view_registrar_recursosHumanos(request):
    if request.method == 'POST':
        decode_json = request.body.decode('utf-8')
        registro_recursosHumanos= json.loads(decode_json)
        banco = RecursosHumano(funcionario=registro_recursosHumanos['funcionario'], cargo=registro_recursosHumanos['cargo'], salario=registro_recursosHumanos['salario'], carga_horaria=registro_recursosHumanos['carga_horaria'], folha_de_ponto=registro_recursosHumanos['folha_de_ponto'], setor=registro_recursosHumanos['setor'])
        banco.save()
        return JsonResponse({
            "status": "Cadastro Realizado com Sucesso",
            "registro": {
                "id": banco.pk,
                "cargo":  registro_recursosHumanos['cargo'],
                "salario":  registro_recursosHumanos['salario'],
                "carga_horaria":  registro_recursosHumanos['carga_horaria'],
                "folha_de_ponto":  registro_recursosHumanos['folha_de_ponto'],
                "setor":  registro_recursosHumanos['setor']
            }
        })
    elif request.method == 'GET':
        query_set = RecursosHumano.objects.all()
        query_serializer = serializers.serialize('json', query_set)
        nomes_json = json.loads(query_serializer)
        resposta_json = parse_json(nomes_json)
        return JsonResponse(resposta_json, safe=False)    
    elif request.method == 'PUT':
        decode_json = request.body.decode('utf-8')
        registro_financeiro = json.loads(decode_json)
        query_set = RecursosHumano.objects.get(pk=registro_financeiro['id'])
        query_set.cargo = registro_financeiro['cargo']
        query_set.salario = registro_financeiro['salario']
        query_set.carga_horaria = registro_financeiro['carga_horaria']
        query_set.folha_de_ponto = registro_financeiro['folha_de_ponto']
        query_set.setor = registro_financeiro['setor']
        query_set.save()
        return JsonResponse({
            "status": "Cadastro Atualizado com sucesso.",
            "registro": {
                "id": query_set.pk,
                "cargo": query_set.cargo,
                "salario": query_set.salario,
                "carga_horaria":  query_set.carga_horaria,
                "folha_de_ponto":  query_set.folha_de_ponto,
                "setor":  query_set.setor
            }
        })
    elif request.method == 'DELETE':
        decode_json = request.body.decode('utf-8')
        registro_recursosHumanos = json.loads(decode_json)
        query_set = RecursosHumano.objects.get(pk=registro_recursosHumanos['id'])
        query_set.delete()

def view_buscar_recursosHumanos(request, id):
    if request.method == 'GET':
        query_set = RecursosHumano.objects.get(pk=id)
        query_serialize = json.loads(serializers.serialize('json', [query_set]))
        resposta_json = parse_json(query_serialize)                                     
    return JsonResponse(resposta_json, safe=False)