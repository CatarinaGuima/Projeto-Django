from django.http import JsonResponse
from django.core import serializers
import json
from database.models import Produto #nome da classe do models de database

# Create your views here.
def parse_json(query_serializer):
    resposta_json = []
    for item in query_serializer:
        itens = {"nome": item['fields']['nome'],
                "quantidade_estoque": item['fields']['quantidade_estoque'],
                "descricao": item['fields']['descricao'],
                "preco": item['fields']['preco'],
                "categoria": item['fields']['categoria'],
                "tipo": item['fields']['tipo'],
        }
        resposta_json.append(itens)
    return resposta_json    

def view_registrar_produtos(request):
    if request.method == 'POST':
        decode_json = request.body.decode('utf-8')
        registro_produto = json.loads(decode_json)
        banco = Produto(nome=registro_produto['nome'], quantidade_estoque=registro_produto['quantidade_estoque'], descricao=registro_produto['descricao'], preco=registro_produto['preco'], categoria=registro_produto['categoria'], tipo=registro_produto['tipo'])
        banco.save()
        return JsonResponse({
            "status": "Cadastro Realizado com Sucesso",
            "registro": {
                "id": banco.pk,
                "nome":  registro_produto['nome'],
                "quantidade_estoque": registro_produto['quantidade_estoque'],
                "descricao": registro_produto['descricao'],
                "preco": registro_produto['preco'],
                "categoria": registro_produto['categoria'],
                "tipo": registro_produto['tipo'],
            }
        })
    elif request.method == 'GET':
        query_set = Produto.objects.all()
        query_serializer = serializers.serialize('json', query_set)
        nomes_json = json.loads(query_serializer)
        resposta_json = parse_json(nomes_json)
        return JsonResponse(resposta_json, safe=False)    
    elif request.method == 'PUT':
        decode_json = request.body.decode('utf-8')
        registro_produto = json.loads(decode_json)
        query_set = Produto.objects.get(pk=registro_produto['id'])
        query_set.nome = registro_produto['nome']
        query_set.quantidade_estoque = registro_produto['quantidade_estoque']
        query_set.descricao = registro_produto['descricao']
        query_set.preco = registro_produto['preco']
        query_set.categoria = registro_produto['categoria']
        query_set.tipo = registro_produto['tipo']
        query_set.save()
        return JsonResponse({
            "status": "Cadastro Atualizado com sucesso.",
            "registro": {
                "id": query_set.pk,
                "nome": query_set.nome,
                "quantidade_estoque": query_set.quantidade_estoque,
                "descricao": query_set.descricao,
                "preco": query_set.preco,
                "categoria": query_set.categoria,
                "tipo": query_set.tipo,
            }
        })
    elif request.method == 'DELETE':
        decode_json = request.body.decode('utf-8')
        registro_financeiro = json.loads(decode_json)
        query_set = Produto.objects.get(pk=registro_financeiro['id'])
        query_set.delete()

def view_buscar_produtos(request, id):
    if request.method == 'GET':
        query_set = Produto.objects.get(pk=id)
        query_serialize = json.loads(serializers.serialize('json', [query_set]))
        resposta_json = parse_json(query_serialize)                                     
    return JsonResponse(resposta_json, safe=False)