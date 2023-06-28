from django.http import JsonResponse
from django.core import serializers
import json
from database.models import Estoque #nome da classe do models de database
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def parse_json(query_serializer):
    resposta_json = []
    for item in query_serializer:
        itens = {
                  "setor": item['fields']['setor'],
                  "corredor": item['fields']['corredor'],
                  "prateleira": item['fields']['prateleira'],
                  "nome_produto": item['fields']['nome_produto'],
                }
        resposta_json.append(itens)
    return resposta_json    

def view_registrar_estoque(request):
    if request.method == 'POST':
        decode_json = request.body.decode('utf-8')
        registro_estoque= json.loads(decode_json)
        banco = Estoque(setor=registro_estoque['setor'], corredor=registro_estoque['corredor'], prateleira=registro_estoque['prateleira'], nome_produto=registro_estoque['nome_produto'])
        banco.save()
        return JsonResponse({
            "status": "Cadastro Realizado com Sucesso",
            "registro": {
                "id": banco.pk,
                "setor":  registro_estoque['setor'],
                "corredor": registro_estoque['corredor'],
                "prateleira": registro_estoque['prateleira'],
                "nome_produto": registro_estoque['nome_produto']
            }
        })
    elif request.method == 'GET':
        query_set = Estoque.objects.all()
        query_serializer = serializers.serialize('json', query_set)
        nomes_json = json.loads(query_serializer)
        resposta_json = parse_json(nomes_json)
        return JsonResponse(resposta_json, safe=False)    
    elif request.method == 'PUT':
        decode_json = request.body.decode('utf-8')
        registro_estoque = json.loads(decode_json)
        query_set = Estoque.objects.get(pk=registro_estoque['id'])
        query_set.setor = registro_estoque['setor']
        query_set.corredor = registro_estoque['corredor']
        query_set.prateleira = registro_estoque['prateleira']
        query_set.nome_produto = registro_estoque['nome_produto']
        query_set.save()
        return JsonResponse({
            "status": "Cadastro Atualizado com sucesso.",
            "registro": {
                "id": query_set.pk,
                "setor": query_set.setor,
                "corredor": query_set.corredor,
                "prateleira": query_set.prateleira,
                "nome_produto": query_set.nome_produto,
            }
        })
    elif request.method == 'DELETE':
        decode_json = request.body.decode('utf-8')
        registro_financeiro = json.loads(decode_json)
        query_set = Estoque.objects.get(pk=registro_financeiro['id'])
        query_set.delete()
        return JsonResponse({"status": "Dado excluído com sucesso."})
    
def view_buscar_estoque(request, id):
    if request.method == 'GET':
     try: 
        query_set = Estoque.objects.get(pk=id)
        query_serialize = json.loads(serializers.serialize('json', [query_set]))
        resposta_json = parse_json(query_serialize)                                     
        return JsonResponse(resposta_json, safe=False)
     except ObjectDoesNotExist:
        # Objeto não encontrado, retornar uma resposta adequada
        return JsonResponse({'error': 'ID não existe.'}, status=404)